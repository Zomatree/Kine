from __future__ import annotations
import asyncio

import contextvars
import pickle
import sys
import subprocess
import multiprocessing

from typing import TYPE_CHECKING, Any, Callable, Coroutine, ParamSpec, TypeVar

from kine import *
from kine.renderers.wasm import App

if TYPE_CHECKING:
    from aiohttp import web

P = ParamSpec("P")
R = TypeVar("R")

api_url = ""

REQUEST: contextvars.ContextVar[web.Request] = contextvars.ContextVar("request")
IS_WEB_PLATFORM = sys.platform == "emscripten"
IS_SERVER_PLATFORM = not IS_WEB_PLATFORM
SERVER_FUNCS: list[Callable[..., Coroutine[Any, Any, Any]]] = []

async def start_fullstack(app_func: ComponentFunction[P], *, host: str = "127.0.0.1", api_port: int = 8000, web_port: int = 8080):
    global api_url

    api_url = f"{host}:{api_port}"

    if IS_WEB_PLATFORM:
        app = App(app_func)
        await app.start()

    else:
        async def api_runner():
            from aiohttp import web
            import aiohttp_cors

            server = web.Application()
            cors = aiohttp_cors.setup(server)

            for func in SERVER_FUNCS:
                async def wrapper(request: web.Request, func: Callable[..., Coroutine[Any, Any, Any]] = func) -> web.Response:
                    REQUEST.set(request)

                    body = await request.read()
                    args, kwargs = pickle.loads(body)

                    try:
                        response = {"response": await func(*args, **kwargs), "failed": False}
                    except BaseException as e:
                        response = {"response": e, "failed": True}

                    return web.Response(body=pickle.dumps(response))

                route = server.router.add_post(f"/{func.__name__}", wrapper)
                cors.add(route, {f"*": aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*", allow_methods="*")})

            await web._run_app(server, port=api_port, host=host, print=lambda _: print(f"Running api on http://{host}:{api_port}"))

        web_p = subprocess.Popen([sys.executable, "-m", "kine", "run", "--host", host, "--port", str(web_port)])
        api_p = multiprocessing.Process(target=lambda: asyncio.run(api_runner()))

        api_p.start()

        web_p.wait()
        api_p.join()

def server(f: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
    if IS_WEB_PLATFORM:
        from pyodide.http import pyfetch

        async def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            resp = await pyfetch(f"http://{api_url}/{f.__name__}", body=pickle.dumps((args, kwargs)), method="POST", headers={"content-type": "application/json"})
            body = pickle.loads(await resp.bytes())
            response = body["response"]

            if body["failed"]:
                raise response
            else:
                return response

        return inner

    else:
        SERVER_FUNCS.append(f)

        return f

def request() -> web.Request:
    try:
        return REQUEST.get()
    except Exception as e:
        e.add_note("request not found, make sure this is ran inside a @server function")
        raise e
