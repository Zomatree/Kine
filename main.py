from kine import *
from kine.renderers.web import *

import asyncio


@component
def btn(cx: Scope):
    return cx.render(button(style="background-color: red")[cx.children])


@component
def app(cx: Scope):
    return cx.render(btn()[p["asd"]])


asyncio.run(start_web(app()))
