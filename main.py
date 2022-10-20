import asyncio
import logging

import aiohttp

from r import *

logging.basicConfig(level=logging.INFO)

@component
def http(cx: Scope):
    session = cx.consume_context(aiohttp.ClientSession)

    async def get():
        request = await session.get("https://httpbin.org/get")
        return await request.json()

    req = use_future(cx, get)
    print(req)
    return cx.render(
        str(req) if req is not None else None
    )

@component
def app(cx: Scope):
    cx.use_hook(lambda: cx.provide_context(aiohttp.ClientSession()))

    return cx.render(
        div()[
            http(),
            "asdas"
        ]
    )

asyncio.run(web.start(app))
