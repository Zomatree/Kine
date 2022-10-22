from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, TypedDict, cast

from typing_extensions import Self, Unpack

if TYPE_CHECKING:
    from .core import Node

__all__ = (
    "Element",
    "div",
    "p",
    "input",
    "button",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
)

class ElementArgs(TypedDict, total=False):
    id: str
    cls: str
    type: str
    style: str

    onclick: Callable[[Any], None]
    oninput: Callable[[Any], None]

class Element:
    def __init__(self, **attributes: Unpack[ElementArgs]):
        self.children: tuple[Node[...], ...] = ()
        self.listeners: dict[str, Callable[[Any], None]] = {}

        for name, value in list(attributes.items()):
            if name.startswith("on"):
                self.listeners[name[2:]] = cast(Callable[[Any], None], value)
                del attributes[name]

        self.attributes = {k: str(v) for k, v in attributes.items()}

    def __getitem__(self, children: Node[...] | tuple[Node[...], ...]) -> Self:
        self.children = children if isinstance(children, tuple) else (children,)

        return self

div = type("div", (Element,), {})
p = type("p", (Element,), {})
input = type("input", (Element,), {})
button = type("button", (Element,), {})
h1 = type("h1", (Element,), {})
h2 = type("h2", (Element,), {})
h3 = type("h3", (Element,), {})
h4 = type("h4", (Element,), {})
h5 = type("h5", (Element,), {})
