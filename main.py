import asyncio
import logging
from typing import TypeVar

from r import *

logging.basicConfig(level=logging.INFO)

T = TypeVar("T")

@component
def app(cx: Scope):
    foo = use_state(cx, 1)
    print(foo, foo.get())

    return cx.render(
        div(cx)[
            String(cx, f"Current value: {foo.get()}"),
            button(cx,
                onclick=lambda _: foo.modify(lambda v: v + 1)
            )[
                String(cx, "Add")
            ],
            button(cx,
                onclick=lambda _: foo.modify(lambda v: v - 1)
            )[
                String(cx, "Minus")
            ],
        ]
    )

asyncio.run(web.start(app))
