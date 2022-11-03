from typing import Callable, Any, TypedDict, Unpack, cast, Generic, TypeVar, Self, Generator

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from ...elements import Element as BaseElement, CGI
from ...core import Node

T = TypeVar("T")

class ElementArgs(TypedDict, Generic[T], total=False):
    onclicked: Callable[[T], Any]
    onchanged: Callable[[T], Any]

    key: str
    placeholder_text: str

class Element(BaseElement, Generic[T]):
    def __init__(self, **attributes: Unpack[ElementArgs[T]]):
        self.children: tuple[Node[...], ...] = ()
        self.listeners: dict[str, Callable[[T], None]] = {}

        for name, value in list(attributes.items()):
            if name.startswith("on"):
                self.listeners[name[2:]] = cast(Callable[[T], None], value)
                del attributes[name]

        self.attributes = {k.replace("_", "-"): str(v) for k, v in attributes.items()}

class button(CGI, Element[Gtk.Button]): pass
class vbox(CGI, Element[Gtk.Box]): pass
class hbox(CGI, Element[Gtk.Box]): pass
class entry(CGI, Element[Gtk.Entry]): pass
class label(CGI, Element[Gtk.Label]): pass
