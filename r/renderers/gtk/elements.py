from typing import Callable, Any, TypedDict, cast, Generic, TypeVar
from typing_extensions import Unpack

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from ...elements import Element as BaseElement, CGI

T = TypeVar("T")

class ElementArgs(TypedDict, Generic[T], total=False):
    onclicked: Callable[[T], Any]
    onchanged: Callable[[T], Any]

    key: str
    placeholder_text: str

class Element(BaseElement, Generic[T]):
    def __init__(self, **attributes: Unpack[ElementArgs[T]]):
        super().__init__(**attributes)

        self.attributes = {k.replace("_", "-"): v for k, v in self.attributes.items()}

class button(CGI, Element[Gtk.Button]): pass
class vbox(CGI, Element[Gtk.Box]): pass
class hbox(CGI, Element[Gtk.Box]): pass
class entry(CGI, Element[Gtk.Entry]): pass
class label(CGI, Element[Gtk.Label]): pass
