from r import *
import asyncio
import aiohttp

def text(cx: Scope, text: str) -> Element:
    return p()[
        text
    ]

def app(cx: Scope) -> Node:
    cx.use_hook(lambda: cx.provide_context(aiohttp.ClientSession()))

    (set_foo, foo) = cx.use_state(1)

    return div(id="foo")[
        text(cx.next_scope(), str(foo)),
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
        spawn_component(cx.next_scope())
    ]

def spawn_component(cx: Scope) -> Node:
    session = cx.consume_context(aiohttp.ClientSession)
    result = cx.use_future(session.get("http://httpbin.org/get"))

    return div()[
        text(cx.next_scope(), str(result))
    ]

asyncio.run(web.start(app))
