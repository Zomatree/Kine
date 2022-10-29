from r import *
import asyncio

@component
def app(cx: Scope):
    return cx.render(p()["Hello World!"])

asyncio.run(web.start(app()))
