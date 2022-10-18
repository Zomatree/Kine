import asyncio
import pathlib
from typing import Any, Awaitable, ParamSpec, cast

from aiohttp import web

from .. import ComponentFunction, messages, utils
from ..dom import VirtualDom

P = ParamSpec("P")

file = pathlib.Path(__file__)

with open(file.parent / "interpreter.js") as f:
    interpreter = f.read()

async def start(app: ComponentFunction[...], headers: str = "", addr: str = "127.0.0.1:8080"):
    web_app = web.Application()

    async def ws_handle(request: web.Request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        dom = VirtualDom(app)
        edits = dom.rebuild()
        await ws.send_json(edits.serialize())

        while True:
            (done,), _ = await asyncio.wait([
                asyncio.ensure_future(dom.wait_for_work()),
                asyncio.ensure_future(cast(Awaitable[dict[str, Any]], ws.receive_json())),
            ], return_when=asyncio.FIRST_COMPLETED)

            if msg := done.result():
                if msg["method"] == "user_event":
                    payload = msg["params"]
                    dom.handle_message(messages.EventMessage(scope_id=None, priority=0, element_id=payload["mounted_dom_id"], name=payload["event"], bubbles=False, data=payload["contents"]))

            mutations = dom.work_with_deadline(lambda: False)

            for mutation in mutations:
                await ws.send_json(mutation.serialize())

    async def index(request: web.Request) -> web.Response:
        return web.Response(body=f"""
<!DOCTYPE html>
<html>
  <head>
    {headers}
  </head>
  <body>
    <div id="main"></div>
    <script>
      var WS_ADDR = "wss://{addr}/app";
      {interpreter}
      main();
    </script>
  </body>
</html>""", content_type="text/html")

    web_app.add_routes([web.get("/app", ws_handle), web.get("/", index)])
    await web._run_app(web_app)
