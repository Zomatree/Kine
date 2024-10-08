∑from __future__ import annotations

import asyncio
import pathlib
from typing import Any, Awaitable, Callable, Literal, ParamSpec, cast

import msgpack
from aiohttp import web

from kine import Scope

from ... import ComponentFunction, messages
from ...dom import VirtualDom
from ...ext.web.cookies import EvalMessage, _Cookies
from ...utils import ROOT_SCOPE
from .elements import *

P = ParamSpec("P")

file = pathlib.Path(__file__)

interpreter = (file.parent / "interpreter.js").read_text()
libs = (file.parent / "libs.js").read_text()

class WebVDom(VirtualDom):
    def __init__(self, app: ComponentFunction[...], custom_messages: asyncio.Queue[EvalMessage]):
        super().__init__(app)
        self.custom_messages = custom_messages


def use_eval(cx: Scope, code: str) -> Callable[[], None]:
    def inner():
        msg = EvalMessage()
        msg.code = code

        dom = cast(WebVDom, cx.scopes.dom)
        dom.custom_messages.put_nowait(msg)
        cx.schedule_update()

    return inner

async def handle_embedded_ws_aiohttp(app: ComponentFunction[P], request: web.Request):
    cookies = request.cookies

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    custom_messages = asyncio.Queue[EvalMessage]()
    dom = WebVDom(app, custom_messages)

    root_scope = dom.scopes.get_scope(ROOT_SCOPE)
    root_scope.provide_context(_Cookies(cookies))

    edits = dom.rebuild()
    await ws.send_bytes(msgpack.dumps(edits.serialize()))

    async def receive_wrapper():
        try:
            return msgpack.loads(await ws.receive_bytes())
        except TypeError:
            return True

    while True:
        futs = await asyncio.wait(
            [
                asyncio.ensure_future(dom.wait_for_work()),
                asyncio.ensure_future(cast(Awaitable[Literal[True] | dict[str, Any]], receive_wrapper())),
                asyncio.ensure_future(custom_messages.get()),
            ],
            return_when=asyncio.FIRST_COMPLETED,
        )

        dones, pending = futs

        for task in pending:
            task.cancel()

        for done in dones:
            try:
                result = done.result()
            except (TypeError, RuntimeError):
                await ws.close()
                return ws

            if result == True:
                await ws.close()
                return ws

            elif isinstance(result, EvalMessage):
                await ws.send_bytes(msgpack.dumps([{"type": "EvalMessage", "code": result.code}]))

            elif msg := result:
                if msg["method"] == "user_event":
                    payload = msg["params"]
                    dom.handle_message(
                        messages.EventMessage(
                            scope_id=None,
                            priority=0,
                            element_id=payload["mounted_dom_id"],
                            name=payload["event"],
                            bubbles=False,
                            data=payload["contents"],
                        )
                    )

            mutations = dom.work_with_deadline()

            for mutation in mutations:
                await ws.send_bytes(msgpack.dumps(mutation.serialize()))

def generate_index(headers: str, ws_addr: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <script>
            {libs}
            </script>
            {headers}
        </head>
        <body>
            <div id="main"></div>
            <script>
            {interpreter}
            main("{ws_addr}");
            </script>
        </body>
    </html>"""

async def start_web(app: ComponentFunction[P], *, host: str = "0.0.0.0:5000", headers: str = "", addr: str = "ws://0.0.0.0:8080"):
    web_app = web.Application()

    async def index(request: web.Request) -> web.Response:
        return web.Response(
            body=generate_index(headers, addr),
            content_type="text/html",
        )

    web_app.add_routes([web.get("/app", lambda r: handle_embedded_ws_aiohttp(app, r)), web.get("/", index)])
    await web._run_app(web_app) #, host=host)  # type: ignore
