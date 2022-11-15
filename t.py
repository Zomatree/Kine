from r.renderers.tui import *
from r import *
import asyncio


@component
def app(cx: Scope):
    return cx.render(container[
        static["hello world"],
        button(
            onclick=lambda _: None
        )[
            
        ]
    ])

asyncio.run(start_tui(app()))
