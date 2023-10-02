from kine import *
from kine.renderers.web import *

import asyncio


@component
def app(cx: Scope):
    return p["Hello World!"]


asyncio.run(start_web(app()))
