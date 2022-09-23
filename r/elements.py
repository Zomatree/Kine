from __future__ import annotations

from typing import Any, TypedDict, Callable, TYPE_CHECKING
from typing_extensions import Self, Unpack

from r.scope import ElementId

if TYPE_CHECKING:
    from .core import Node

__all__ = (
    "Element",
    "div",
    "p",
    "button"
)

class ElementArgs(TypedDict, total=False):
    id: str
    cls: str

    onclick: Callable[[dict], None]

class Element:
    def __init__(self, **attributes: Unpack[ElementArgs]):
        self.children: tuple[Node] = tuple()
        self.handlers: dict[str, Any] = {}

        self.id: ElementId | None = None

        for name, value in list(attributes.items()):
            if name.startswith("on"):
                self.handlers[name] = value
                del attributes[name]

        self.attributes = {k: str(v) for k, v in attributes.items()}

    def __getitem__(self, children: Node | tuple[Node, ...]) -> Self:
        self.children = children if isinstance(children, tuple) else (children,)
        return self

class div(Element):
    pass

class p(Element):
    pass

class button(Element):
    pass
