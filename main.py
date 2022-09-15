from r import *
import asyncio

@component
def text(cx: Scope, text: str) -> Element:
    return p()[
        text
    ]

@component
def app(cx: Scope) -> Node:
    (set_foo, foo) = cx.use_state(1)

    return div(id="foo")[
        text(cx, str(foo)),
        button(
            onclick=lambda _: set_foo(foo + 1)
        )[
            "Add"
        ],
        button(
            onclick=lambda _: set_foo(foo - 1)
        )[
            "Minus"
        ],
    ]

asyncio.run(web.start(app))
