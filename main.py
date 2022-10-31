import asyncio

from r import *
from r.renderers.gtk import *

@component
def app(cx: Scope):
    return cx.render(vbox()[
        label()["hello world"],
        button(onclicked=print)["click me"]
    ])

asyncio.run(start_gtk(app()))
