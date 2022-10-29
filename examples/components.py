import asyncio
from dataclasses import dataclass
from typing import Any, Callable

from r import *


@dataclass
class Item:
    id: int
    title: str
    description: str

ItemState: Callable[[], dict[int, Item]] = lambda: {}

@component
def item(cx: Scope, item_id: int):
    item_state = use_read(cx, ItemState)
    item = item_state[item_id]

    return cx.render(div()[
        h3()[
            item.title
        ],
        p()[
            item.description
        ]
    ])

@component
def add_item(cx: Scope):
    item_state = use_read(cx, ItemState)
    set_item_state = use_set(cx, ItemState)

    title = use_state(cx, lambda: "")
    description = use_state(cx, lambda: "")

    def update_items(_: Any):
        id = len(item_state)
        item_state[id] = Item(id, title.get(), description.get())
        set_item_state(item_state)

    return cx.render(div()[
        h3()[
            "Title"
        ],
        input(
            type="text",
            oninput=lambda evt: title.set(evt["value"])
        ),
        h3()[
            "Description"
        ],
        input(
            type="text",
            oninput=lambda evt: description.set(evt["value"])
        ),
        button(
            onclick=update_items
        )[
            "Create"
        ]
    ])

@component
def app(cx: Scope):
    item_state =  use_read(cx, ItemState)
    print("app ", item_state)

    return cx.render(div()[
        add_item(),
        div()[
            (item(item_id).key(str(item_id)) for item_id in item_state.keys())
        ]
    ])

asyncio.run(web.start(app()))
