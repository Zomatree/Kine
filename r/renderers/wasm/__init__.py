from __future__ import annotations

from typing import TYPE_CHECKING, ParamSpec
import js
from pyodide.ffi import create_proxy
import asyncio

from ... import ComponentFunction, messages, diff
from ...dom import VirtualDom, ElementId

from ..web_elements import *
from .components import *

P = ParamSpec("P")

async def start_wasm(app: ComponentFunction[P]):
    dom = VirtualDom(app)

    edits = dom.rebuild()

    event_queue = asyncio.Queue[Any]()
    main = js.document.getElementById("main")

    if not main:
        raise Exception("No element with id of main")

    nodes: dict[ElementId, js.Element | js.Text] = {ElementId(0): main}

    calculate_diffs(event_queue, nodes, edits)

    while True:
            futs = await asyncio.wait([
                asyncio.ensure_future(dom.wait_for_work()),
                asyncio.ensure_future(event_queue.get()),
            ], return_when=asyncio.FIRST_COMPLETED)
            dones, pending = futs

            for task in pending:
                task.cancel()

            for done in dones:
                try:
                    result = done.result()
                except TypeError:
                    return

                if msg := result:
                    if msg["method"] == "user_event":
                        payload = msg["params"]
                        dom.handle_message(messages.EventMessage(scope_id=None, priority=0, element_id=payload["mounted_dom_id"], name=payload["event"], bubbles=False, data=payload["contents"]))

                mutations = dom.work_with_deadline(lambda: False)

                for mutation in mutations:
                    calculate_diffs(event_queue, nodes, mutation)

def calculate_diffs(queue: asyncio.Queue[Any], nodes: dict[ElementId, js.Element | js.Text], mutation: diff.Mutations):
    for mod in mutation.modifications:
        match mod:
            case diff.AppendChildren():
                node = nodes[mod.root]

                for child in mod.children:
                    node.appendChild(nodes[child])

            case diff.ReplaceWith():
                node = nodes[mod.root]
                if TYPE_CHECKING:
                    assert isinstance(node, js.Element)

                elements = [nodes[id] for id in mod.nodes]
                node.replaceWith(*elements)

            case diff.CreateElement():
                element = js.document.createElement(mod.tag)
                nodes[mod.root] = element

            case diff.CreateTextNode():
                element = js.document.createTextNode(mod.text)
                nodes[mod.root] = element

            case diff.NewEventListener():
                def callback(evt: Any, mod: diff.NewEventListener = mod):
                    data = evt.to_py()
                    js.console.log(str(data))

                    queue.put_nowait({
                        "method": "user_event",
                        "params": {
                            "event": mod.event_name,
                            "mounted_dom_id": mod.root,
                            "contents": data
                        }
                    })

                proxy_func = create_proxy(callback)

                node = nodes[mod.root]
                if TYPE_CHECKING:
                    assert isinstance(node, js.Element)
                node.setAttribute("data-r-id", str(mod.root))
                node.addEventListener(mod.event_name, proxy_func)

            case diff.SetText():
                node = nodes[mod.root]
                if TYPE_CHECKING:
                    assert isinstance(node, js.Text)
                node.data = mod.text

            case diff.SetAttribute():
                node = nodes[mod.root]

                if TYPE_CHECKING:
                    assert isinstance(node, js.Element)

                if mod.field == "value":
                    if TYPE_CHECKING:
                        assert isinstance(node, js.HTMLInputElement)

                    if mod.value != node.value:
                        node.value = mod.value

                else:
                    node.setAttribute(mod.field, mod.value)

            case diff.InsertAfter():
                node = nodes[mod.root]
                if TYPE_CHECKING:
                    assert isinstance(node, js.Element)
                elements = [nodes[id] for id in mod.nodes]
                node.after(*elements)

            case diff.Remove():
                node = nodes[mod.root]
                if TYPE_CHECKING:
                    assert isinstance(node, js.Element)
                node.remove()

            case diff.InsertBefore():
                node = nodes[mod.root]
                if TYPE_CHECKING:
                    assert isinstance(node, js.Element)
                elements = [nodes[id] for id in mod.nodes]
                node.before(*elements)

            case diff.CreatePlaceholder():
                node = js.document.createElement("pre")

                if TYPE_CHECKING:
                    assert isinstance(node, js.HTMLElement)

                node.hidden = True
                nodes[mod.root] = node

            case diff.RemoveAttribute():
                node = nodes[mod.root]

                if mod.field == "value":
                    if TYPE_CHECKING:
                        assert isinstance(node, js.HTMLInputElement)

                    node.value = ""
                else:
                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)
                    node.removeAttribute(mod.field)

            case _:
                raise Exception(str(mod))
