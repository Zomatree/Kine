from asyncio import events
from typing import ParamSpec, cast

from r.utils import ElementId

from ... import ComponentFunction, diff, messages
from ...dom import VirtualDom
from ...diff import Mutations

from textual.app import App as BaseApp, ComposeResult
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import *
from textual.message import Message as TextualMessage
from textual import events

from .elements import *

P = ParamSpec("P")

class App(BaseApp[None]):
    def __init__(self, dom: VirtualDom) -> None:
        super().__init__()
        self.nodes: dict[ElementId, Widget | str] = {}
        self.element_ids: dict[Widget, ElementId] = {}

        self.dom = dom

    async def on_mount(self, event: events.Mount):
        id = ElementId(0)
        self.nodes[id] = main = self.query_one("#main")
        self.element_ids[main] = id

        mutations = self.dom.rebuild()

        await self.handle_mutations(mutations)

    async def handle_mutations(self, mutations: Mutations):
        for mod in mutations.modifications:
            print(mod)
            match mod:
                case diff.CreateElement():
                    self.nodes[mod.root] = widget = self.create_widget(mod.tag)
                    self.element_ids[widget] = mod.root

                case diff.CreateTextNode():
                    self.nodes[mod.root] = mod.text

                case diff.AppendChildren():
                    parent = self.nodes[mod.root]
                    assert not isinstance(parent, str)
                    children: list[Widget] = []

                    for child_id in mod.children:
                        child = self.nodes[child_id]
                        if isinstance(child, str):
                            if isinstance(parent, Button):
                                parent.label = child
                            elif isinstance(parent, Static):
                                parent.renderable = child
                                assert isinstance(parent, Static)
                        else:
                            children.append(child)

                    await parent.mount(*children)

                case diff.NewEventListener():
                    node = self.nodes[mod.root]
                    assert isinstance(node, Widget)

                    def press(event: TextualMessage, *, node: Widget = node, event_name: str = mod.event_name):
                        element_id = self.element_ids[cast(Widget, event.sender)]
                        self.dom.handle_message(messages.EventMessage(None, 0, element_id, event_name, True, event))

                    setattr(node, f"_on_button_{mod.event_name}", event_handler)

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
            case "input":
                return Input()
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
