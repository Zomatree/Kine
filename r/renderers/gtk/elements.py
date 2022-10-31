from typing import Callable, Any, TypedDict, Unpack, cast

from ...elements import Element as BaseElement
from ...core import Node

class ElementArgs(TypedDict, total=False):
    onclicked: Callable[[Any], None]

class Element(BaseElement):
    def __init__(self, **attributes: Unpack[ElementArgs]):
        self.children: tuple[Node[...], ...] = ()
        self.listeners: dict[str, Callable[[Any], None]] = {}

        for name, value in list(attributes.items()):
            if name.startswith("on"):
                self.listeners[name[2:]] = cast(Callable[[Any], None], value)
                del attributes[name]

        self.attributes = {k: str(v) for k, v in attributes.items()}

button = type("button", (Element,), {})
label = type("label", (Element,), {})
vbox = type("vbox", (Element,), {})
hbox = type("hbox", (Element,), {})
