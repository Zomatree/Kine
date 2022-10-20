import asyncio
import logging

from r import *

logging.basicConfig(level=logging.INFO)


@component
def app(cx: Scope):
    name = use_state(cx, lambda: "")
    clicked = use_state(cx, lambda: False)

    return cx.render(
        div()[
            input(
                type="text",
                oninput=lambda evt: name.set(evt["value"])
            ),
            button(
                onclick=lambda _: clicked.modify(lambda v: not v)
            )[
                "Enter"
            ],
            p()[f"hello {name.get()}"] if clicked.get() else None
        ]
    )

asyncio.run(web.start(app))
