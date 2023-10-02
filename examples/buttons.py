from kine import *
from kine.renderers.web import *

import asyncio


@component
def app(cx: Scope):
    value = use_state(cx, lambda: 0)

    return div[
        button(
            onclick=lambda _: value.modify(lambda v: v - 1)
        )[
            "Minus"
        ],
        str(value.get()),
        button(
            onclick=lambda _: value.modify(lambda v: v + 1)
        )[
            "Add"
        ]
    ]


asyncio.run(start_web(app()))
