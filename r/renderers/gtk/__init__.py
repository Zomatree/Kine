import asyncio
from typing import ParamSpec
import threading

from ... import ComponentFunction, diff, messages
from ...dom import VirtualDom
from ...diff import Mutations
from ...utils import ElementId
from .elements import *

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

P = ParamSpec("P")

class App(Adw.Application):
    def __init__(self, dom: VirtualDom, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

        self.dom = dom
        self.nodes: dict[ElementId, Gtk.Widget | str] = {}
        self.parents: dict[ElementId, Gtk.Widget] = {}

    def on_activate(self, app: Gtk.Application):
        self.win = Gtk.ApplicationWindow(application=app)
        self.win.present()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.win.set_child(box)

        self.nodes[ElementId(0)] = box

        mods = self.dom.rebuild()
        self.calculate_diffs(mods)

        self.bg_thread = threading.Thread(target=lambda: asyncio.run(self.bg_loop()))
        self.bg_thread.start()

    async def bg_loop(self):
        while True:
            await self.dom.wait_for_work()
            mutations = self.dom.work_with_deadline(lambda: False)

            for mutation in mutations:
                self.calculate_diffs(mutation)

    def calculate_diffs(self, mutations: Mutations):
        for mod in mutations.modifications:
            match mod:
                case diff.CreateElement():
                    widget = self.create_widget(mod.tag)
                    self.nodes[mod.root] = widget

                case diff.CreateTextNode():
                    self.nodes[mod.root] = mod.text

                case diff.AppendChildren():
                    for child_id in mod.children:
                        self.add_node_child(mod.root, child_id)

                case diff.NewEventListener():
                    parent = self.nodes[mod.root]
                    parent.connect(mod.event_name, self.call_event(mod.root, mod.event_name))

                case diff.SetText():
                    node = self.parents[mod.root]

                    assert not isinstance(node, str)

                    self.set_node_label(node, mod.text)

                case diff.SetAttribute():
                    if mod.field == "key":
                        continue

                    node = self.nodes[mod.root]

                    if isinstance(node, Gtk.Widget):
                        node.set_property(mod.field, mod.value)

                case diff.InsertAfter():
                    parent = self.parents[mod.root]
                    before_node = self.nodes[mod.root]

                    for element_id in mod.nodes:
                        node = self.nodes[element_id]
                        self.parents[element_id] = parent

                        node.set_parent(parent)
                        parent.insert_child_after(before_node, node)

                case diff.Remove():
                    parent = self.parents[mod.root]
                    widget = self.nodes[mod.root]
                    parent.remove(widget)

                case _:
                    raise Exception(mod)

    def add_node_child(self, parent_id: ElementId, child_id: ElementId):
        parent = self.nodes[parent_id]
        assert not isinstance(parent, str)

        self.parents[child_id] = parent
        child = self.nodes[child_id]

        if isinstance(child, str):
            self.set_node_label(parent, child)
        else:
            parent.append(child)
            child.set_parent(parent)

    def set_node_label(self, node: Gtk.Widget, text: str):
        if isinstance(node, Gtk.Label):
            node.set_text(text)
        else:
            node.set_label(text)

    def call_event(self, element_id: ElementId, name: str):
        def inner(widget: Gtk.Widget):
            self.dom.temp.append(messages.EventMessage(None, 0, element_id, name, True, widget))

        return inner

    def create_widget(self, name: str) -> Gtk.Widget:
        match name:
            case "label":
                return Gtk.Label()
            case "vbox":
                return Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            case "hbox":
                return Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            case "button":
                return Gtk.Button()
            case "entry":
                return Gtk.Entry()
            case _:
                raise Exception(name)

async def start_gtk(app: ComponentFunction[P], window_size: tuple[int, int] = (1280, 720)):
    dom = VirtualDom(app)

    app = App(dom)
    app.run()
