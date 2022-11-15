from r.renderers.tui import *
from r import *
import asyncio


@component
def app(cx: Scope):
    return cx.render(container[
        button["+1"],
    ])

asyncio.run(start_tui(app()))
