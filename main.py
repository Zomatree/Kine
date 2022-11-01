import asyncio

from r import *
from r.renderers.gtk import *

@component
def app(cx: Scope):
    value = use_state(cx, lambda: 0)

    return cx.render(vbox()[
        button(
            onclicked=lambda _: value.modify(lambda x: x - 1)
        )[
            "Minus"
        ],
        label()[
            f"{value.get()}"
        ],
        button(
            onclicked=lambda _: value.modify(lambda x: x + 1)
        )[
            "Add"
        ]
    ])

asyncio.run(start_gtk(app()))
