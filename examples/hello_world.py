from r import *
from r.renderers.web import *

import asyncio

@component
def app(cx: Scope):
    return cx.render(p()["Hello World!"])

asyncio.run(start_web(app()))
