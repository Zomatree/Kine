from kine import *
from kine.renderers.web import *

import aiohttp
import asyncio

@component
def app(cx: Scope):
    session = cx.use_hook(lambda: aiohttp.ClientSession())

    async def http_request():
        async with session.get("https://httpbin.org/get") as req:
            return await req.json()

    future = use_future(cx, http_request)

    return cx.render(div[
        p[
            "Http request result:"
        ],
        p[
            str(future.value) if future.value is not None else "Loading..."
        ]
    ])

asyncio.run(start_web(app()))
