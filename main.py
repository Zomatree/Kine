from r import *
import asyncio

@component
def text(cx: Scope, text: str) -> Element:
    return p()[
        String(text)
    ]

def app(cx: Scope) -> Node[...]:
    foo = cx.use_state(1)

    return div(id="foo")[
        text(str(foo)),
        button(
            onclick=lambda _: foo.modify(lambda v: v + 1)
        )[
            String("Add")
        ],
        button(
            onclick=lambda _: foo.modify(lambda v: v - 1)
        )[
            String("Minus")
        ]
    ]

asyncio.run(web.start(app))
