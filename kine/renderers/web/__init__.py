from __future__ import annotations

import asyncio
import pathlib
from typing import Any, Awaitable, Literal, ParamSpec, cast

from aiohttp import web
from kine import Scope
import msgpack
from ...ext.web.cookies import _Cookies, EvalMessage

from ...utils import ScopeId
from ... import ComponentFunction, messages
from ...dom import VirtualDom

from ..web_elements import *

P = ParamSpec("P")

file = pathlib.Path(__file__)

with open(file.parent / "interpreter.js") as f:
    interpreter = f.read()


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


async def start_web(app: ComponentFunction[P], headers: str = "", addr: str = "127.0.0.1:8080"):
    web_app = web.Application()

    async def ws_handle(request: web.Request):
        cookies = request.cookies

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        custom_messages = asyncio.Queue[EvalMessage]()
        dom = WebVDom(app, custom_messages)

        root_scope = dom.scopes.get_scope(ScopeId(0))
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

                mutations = dom.work_with_deadline(lambda: False)

                for mutation in mutations:
                    await ws.send_bytes(msgpack.dumps(mutation.serialize()))

    async def index(request: web.Request) -> web.Response:
        return web.Response(
            body=f"""
<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/msgpack-lite/0.1.26/msgpack.min.js" integrity="sha512-harMiusNxs02ryf3eqc3iQalz2RSd0z38vzOyuFwvQyW046h2m+/47WiDmPW9soh/p71WQMRSkhSynEww3/bOA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/3.0.1/js.cookie.min.js" integrity="sha512-wT7uPE7tOP6w4o28u1DN775jYjHQApdBnib5Pho4RB0Pgd9y7eSkAV1BTqQydupYDB9GBhTcQQzyNMPMV3cAew==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        {headers}
    </head>
    <body>
        <div id="main"></div>
        <script>
        {interpreter}
        main("ws://{addr}/app");
        </script>
    </body>
</html>""",
            content_type="text/html",
        )

    web_app.add_routes([web.get("/app", ws_handle), web.get("/", index)])
    await web._run_app(web_app)  # type: ignore
