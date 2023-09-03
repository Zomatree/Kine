from kine import *
from kine.renderers.web import *

import asyncio
from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    description: str


items: Signal[dict[int, Item]] = signal(lambda: {})

@component
def item(cx: Scope, item: Item):
    return cx.render(div[
        h3[item.title],
        p[item.description]
    ])


@component
def add_item(cx: Scope):
    title = use_state(cx, lambda: "")
    description = use_state(cx, lambda: "")

    def update_items(items: dict[int, Item]):
        id = len(items)

        items[id] = Item(id, title.get(), description.get())

    return cx.render(
        div[
            h3["Title"],
            input(type="text", oninput=lambda evt: title.set(evt["value"])),
            h3["Description"],
            input(type="text", oninput=lambda evt: description.set(evt["value"])),
            button(onclick=lambda _: items.mutate(cx, update_items))["Create"],
        ]
    )


@component
def app(cx: Scope):
    item_state = use_read_signal(cx, items)

    return cx.render(div[
        add_item(),
        div[(
            item(it).key(str(it.id)) for it in item_state.values())
        ]
    ])


asyncio.run(start_web(app()))
