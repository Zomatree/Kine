import asyncio
from asyncio import events
from typing import ParamSpec
from r.core import VNode

from r.utils import ElementId

from ... import ComponentFunction, diff, messages
from ...dom import VirtualDom
from ...diff import Mutations

from textual.app import App as BaseApp, ComposeResult
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import *
from textual import events

from .elements import *

P = ParamSpec("P")

class App(BaseApp[None]):
    def __init__(self, dom: VirtualDom) -> None:
        super().__init__()
        self.nodes: dict[ElementId, Widget | str] = {}
        self.dom = dom

    def on_mount(self, event: events.Mount):
        self.nodes[ElementId(0)] = self.query_one("#main")
        mutations = self.dom.rebuild()

        self.handle_mutations(mutations)

    def handle_mutations(self, mutations: Mutations):
        for mod in mutations.modifications:
            match mod:
                case diff.CreateElement():
                    widget = self.create_widget(mod.tag)
                    self.nodes[mod.root] = widget

                case diff.CreateTextNode():
                    self.nodes[mod.root] = mod.text

                case diff.AppendChildren():
                    parent = self.nodes[mod.root]
                    assert not isinstance(parent, str)

                    for child_id in mod.children:
                        child = self.nodes[child_id]
                        print(parent, child)
                        if isinstance(child, str):
                            if isinstance(parent, Button):
                                parent.label = child
                            elif isinstance(parent, Static):
                                parent.renderable = child
                                assert isinstance(parent, Static)
                        else:
                            parent._add_child(child)

                    self.refresh()

                case diff.NewEventListener():
                    node = self.nodes[mod.root]

                    async def event_callback(event, *, event_name: str = mod.event_name):
                        node.label = "+2"
                        getattr(type(node), f"_on_{event_name}")(node, event)

                    setattr(node, f"_on_{mod.event_name}", event_callback)
                case _:
                    raise Exception(str(mod))

    def create_widget(self, tag: str) -> Widget:
        match tag:
            case "container":
                return Container()
            case "static":
                return Static()
            case "button":
                return Button(variant="success")
            case "header":
                return Header()
            case "footer":
                return Footer()
            case _:
                raise Exception(str(tag))

    def compose(self) -> ComposeResult:
        yield Widget(id="main")

async def start_tui(app: ComponentFunction[P]):
    dom = VirtualDom(app)
    tui_app = App(dom)

    await tui_app.run_async()
