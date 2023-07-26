import json
import sys
import os
import subprocess

from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from kine import *
from kine.renderers.wasm import App

P = ParamSpec("P")
R = TypeVar("R")

api_url = ""

WEB_PLATFORM = "emscripten"
SERVER_FUNCS: list[Callable[..., Coroutine[Any, Any, Any]]] = []

async def start_fullstack(app_func: ComponentFunction[P], *, host: str = "127.0.0.1", api_port: int = 8000, web_port: int = 8080):
    global api_url

    api_url = f"{host}:{api_port}"

    if sys.platform == WEB_PLATFORM:
        app = App(app_func)
        await app.start()

    elif os.environ.get("KINE_RUN_API", None):
        from aiohttp import web
        import aiohttp_cors

        server = web.Application()
        cors = aiohttp_cors.setup(server)

        for func in SERVER_FUNCS:
            async def wrapper(request: web.Request, func: Callable[..., Coroutine[Any, Any, Any]] = func) -> web.Response:
                body = await request.json()

                response = await func(*body["args"], **body["kwargs"])

                return web.Response(text=json.dumps(response), headers={"content-type": "application/json"})

            route = server.router.add_post(f"/{func.__name__}", wrapper)
            cors.add(route, {f"*": aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*", allow_methods="*")})

        await web._run_app(server, port=api_port, host=host)

    else:
        web_p = subprocess.Popen([sys.executable, "-m", "kine", "run", "--host", host, "--port", str(web_port)])
        api_p = subprocess.Popen([sys.executable, "-c", "import src, asyncio; asyncio.run(src.main())"], env={**os.environ, "KINE_RUN_API": "1"})

        web_p.wait()
        api_p.wait()

def server(f: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
    if sys.platform == WEB_PLATFORM:
        from pyodide.http import pyfetch

        async def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            global api_url

            resp = await pyfetch(f"http://{api_url}/{f.__name__}", body=json.dumps({"args": args, "kwargs": kwargs}), method="POST", headers={"content-type": "application/json"})
            return await resp.json()

        return inner

    else:
        SERVER_FUNCS.append(f)

        return f
