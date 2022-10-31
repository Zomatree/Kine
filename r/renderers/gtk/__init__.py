import asyncio
from typing import ParamSpec

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

    def on_activate(self, app: Gtk.Application):
        self.win = Gtk.ApplicationWindow(application=app)
        self.win.present()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.win.set_child(box)

        self.nodes[ElementId(0)] = box

        mods = self.dom.rebuild()
        self.calculate_diffs(mods)

    def calculate_diffs(self, mutations: Mutations):
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
                    assert not isinstance(parent, str)
                    print(parent)
                    for child_id in mod.children:
                        child = self.nodes[child_id]
                        print(child)

                        if isinstance(child, str):
                            if isinstance(parent, Gtk.Label):
                                parent.set_text(child)
                            else:
                                parent.set_label(child)
                        else:
                            parent.append(child)

                case diff.NewEventListener():
                    parent = self.nodes[mod.root]
                    parent.connect(mod.event_name, self.call_event(mod.root, mod.event_name))

                case _:
                    raise Exception(mod)

    def call_event(self, element_id: ElementId, name: str):
        def inner(widget: Gtk.Widget):
            self.dom.pending_messages.appendleft(messages.EventMessage(None, 0, element_id, name, True, widget))

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
            case _:
                raise Exception(name)

async def start_gtk(app: ComponentFunction[P], window_size: tuple[int, int] = (1280, 720)):
    dom = VirtualDom(app)

    app = App(dom)
    app.run()
