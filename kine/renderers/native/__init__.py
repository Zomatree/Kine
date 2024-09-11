from __future__ import annotations
import time

from kine import Element as BaseElement
from stretchable.style import *

from kine.elements import CGI
from kine.renderers.native.node import RootNode

import threading

from .events import *
from .node import *
from .utils import *
from .window import *

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Generic, ParamSpec, TypedDict, Unpack

from ... import ComponentFunction, diff, messages
from ...dom import ElementId, VirtualDom
from ...utils import ROOT_ELEMENT
from .node import *

P = ParamSpec("P")


class GlobalEvent(TypedDict):
    callback: Callable[[BaseEvent], Any]
    active: int


class AppWindow(Window, Generic[P]):
    def __init__(self, app: App[P], title: str, width: int, height: int):
        self.app = app

        super().__init__(title, width, height)
        self.redraw_event = threading.Event()
        
        self.window: glfw.Window
        
    def nodes(self) -> RootNode:
        return self.app.nodes[ROOT_ELEMENT]
    
    async def background_task(self):
        self.app.loop = asyncio.get_running_loop()
        edits = self.app.dom.rebuild()
        self.app.calculate_diffs(edits)

        while True:
            futs = await asyncio.wait(
                [
                    asyncio.ensure_future(self.app.dom.wait_for_work()),
                    asyncio.ensure_future(self.app.event_queue.get())
                ],
                return_when=asyncio.FIRST_COMPLETED,
            )

            dones, pending = futs

            for task in pending:
                task.cancel()

            for done in dones:
                if (msg := done.result()) and msg is not True and msg["method"] == "user_event":
                        print(msg)
                        payload = msg["params"]
                        self.app.dom.handle_message(
                            messages.EventMessage(
                                scope_id=None,
                                priority=0,
                                element_id=payload["mounted_dom_id"],
                                name=payload["event"],
                                bubbles=False,
                                data=payload["contents"],
                            )
                        )

                mutations = self.app.dom.work_with_deadline()

                for mutation in mutations:
                    self.app.calculate_diffs(mutation)
                    
                glfw.post_empty_event()

    def run_app(self):
        threading.Thread(target=lambda: asyncio.run(self.background_task())).start()

        with glfw_window(self.width, self.height, self.title) as window:
            self.window = window
            glfw.set_window_size_callback(window, self.on_resize)
            glfw.set_mouse_button_callback(window, self.on_click)
            
            while not glfw.window_should_close(window):
                glfw.wait_events()
                
                self.redraw(window)

class App(Generic[P]):
    def __init__(self, app: ComponentFunction[P]) -> None:
        self.dom = VirtualDom(app)
        self.locals: dict[ElementId, dict[str, Callable[..., Any]]] = {}
        self.event_queue = asyncio.Queue[Any]()

        self.nodes: dict[ElementId, Node] = {ROOT_ELEMENT: Node(id=ROOT_ELEMENT)}
        self.window = AppWindow(self, "Test", 800, 600)
        self.loop: asyncio.AbstractEventLoop


    def start(self):
        self.window.run_app()

    def calculate_diffs(self, mutation: diff.Mutations):
        for mod in mutation.modifications:
            print(mod)
            match mod:
                case diff.AppendChildren():
                    node = self.nodes[mod.root]

                    for child in mod.children:
                        node.add(self.nodes[child])

                case diff.ReplaceWith():
                    node = self.nodes[mod.root]

                    elements = [self.nodes[id] for id in mod.nodes]
                    node.replace_with(*elements)

                case diff.CreateElement():
                    element = self.create_element(mod.tag)
                    element.id = mod.root
                    self.nodes[mod.root] = element

                    if ref := mod.ref:
                        ref.value = element

                case diff.CreateTextNode():
                    element = self.create_text_element(mod.text)
                    element.id = mod.root
                    self.nodes[mod.root] = element

                case diff.NewEventListener():
                    def callback(event: Any, node_id: ElementId = mod.root, name: str = mod.event_name):
                        print(event, node_id, mod)
                        asyncio.run_coroutine_threadsafe(
                            self.event_queue.put(
                                {
                                    "method": "user_event",
                                    "params": {
                                        "event": name,
                                        "mounted_dom_id": node_id,
                                        "contents": event
                                    }
                                }
                            ),
                            self.loop
                        )

                    node = self.nodes[mod.root]
                    node.add_event_listener(mod.event_name, callback)
                    self.locals.setdefault(mod.root, {})[mod.event_name] = callback

                case diff.SetText():
                    node = self.nodes[mod.root]
                    
                    if isinstance(node, TextNode):
                        node.text = mod.text

                case diff.SetAttribute():
                    node = self.nodes[mod.root]
                    node.set_attribute(mod.field, mod.value)

                case diff.InsertAfter():
                    node = self.nodes[mod.root]

                    elements = [self.nodes[id] for id in mod.nodes]
                    node.after(*elements)

                case diff.Remove():
                    node = self.nodes[mod.root]

                    node.remove_node()

                case diff.InsertBefore():
                    node = self.nodes[mod.root]

                    elements = [self.nodes[id] for id in mod.nodes]
                    
                    node.before(*elements)

                case diff.CreatePlaceholder():
                    node = self.create_element("div")

                    self.nodes[mod.root] = node

                case diff.RemoveAttribute():
                    node = self.nodes[mod.root]
                    
                    node.remove_attribute(mod.field)

                case diff.RemoveEventListener():
                    node = self.nodes[mod.root]

                    node.remove_event_listener(mod.event_name, self.locals[mod.root][mod.event_name])

                case diff.RemoveAllChildren():
                    node = self.nodes[mod.root]

                    node.clear()

    def create_element(self, tag: str) -> Node:
        match tag:
            case "div":
                return Node()
            case "hstack":
                return HStack()
            case "vstack":
                return VStack()
            case "button":
                return Button()
            case _:
                raise Exception

    def create_text_element(self, text: str) -> TextNode:
        return TextNode(text)

class ElementArgs(TypedDict, total=False):
    onclick: Callable[[MouseEvent], Any]
    font_size: int
    spacing: int
    foreground: Color
    background: Color
    padding: int

class InnnerElement(BaseElement):
    def __init__(self, **attributes: Unpack[ElementArgs]):
        super().__init__(**attributes)

class Element(CGI, InnnerElement):
    pass

class div(Element):
    pass

class hstack(Element):
    pass

class vstack(Element):
    pass

class button(Element):
    pass

def start_native(app_func: ComponentFunction[P]):
    app = App(app_func)
    app.start()
