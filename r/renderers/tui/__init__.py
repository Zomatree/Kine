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
from textual.widgets import Static, Button
from textual import events

from .elements import *

P = ParamSpec("P")

class App(BaseApp[None]):
    def __init__(self, dom: VirtualDom) -> None:
        super().__init__()
        self.nodes: dict[ElementId, Widget | str] = {}
        self.dom = dom

    def on_mount(self, event: events.Mount):
        main = self.query_one("#main")
        main._parent = self.screen
        self.nodes[ElementId(0)] = main
        mutations = self.dom.rebuild()

        self.handle_mutations(mutations)

    def handle_mutations(self, mutations: Mutations):
        for mod in mutations.modifications:
            print(mod)

            match mod:
                case diff.CreateElement():
                    widget = self.create_widget(mod.tag)
                    self.nodes[mod.root] = widget

                case diff.CreateTextNode():
                    self.nodes[mod.root] = mod.text

                case diff.AppendChildren():
                    parent = self.nodes[mod.root]
                    assert isinstance(parent, Widget)

                    for child_id in mod.children:
                        child = self.nodes[child_id]

                        if isinstance(child, str):
                            assert isinstance(parent, Static)
                            parent.renderable = child
                        else:
                            parent.children._append(child)
                            child._parent = parent

                case diff.NewEventListener():
                    node = self.nodes[mod.root]
                    def event_callback(event):
                        print(event)

                    setattr(node, f"_on_{mod.event_name}", event)
                case _:
                    raise Exception(str(mod))

    def create_widget(self, tag: str) -> Widget:
        match tag:
            case "container":
                return Container()
            case "static":
                return Static()
            case "button":
                return Button()
            case _:
                raise Exception(str(tag))

    def compose(self) -> ComposeResult:
        yield Container(id="main")

async def start_tui(app: ComponentFunction[P]):
    dom = VirtualDom(app)
    tui_app = App(dom)

    await tui_app.run_async()
