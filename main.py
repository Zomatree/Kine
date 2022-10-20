import asyncio
import logging

from r import *

logging.basicConfig(level=logging.INFO)

@component
def my_component(cx: Scope):
    name = use_state(cx, lambda: "")

    return cx.render(
        div()[
            input(
                type="text",
                oninput=lambda evt: name.set(evt["value"])
            ),
            p()[
                f"Hello {name.get()}"
            ]
        ]
    )

@component
def app(cx: Scope):

    return cx.render(
        div()[
            my_component(),
            "asdas"
        ]
    )

asyncio.run(web.start(app, addr="zomatree-r-q955j7vq49gf49qr-8080.githubpreview.dev"))
