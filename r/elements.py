from __future__ import annotations

from typing import TypedDict, Callable, TYPE_CHECKING
from typing_extensions import Self, Unpack

if TYPE_CHECKING:
    from .r import Node

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
    def __init__(self, **props: Unpack[ElementArgs]):
        self.children: tuple[Node] = tuple()
        self.props = props

    def __getitem__(self, children: Node | tuple[Node, ...]) -> Self:
        self.children = children if isinstance(children, tuple) else (children,)
        return self

class div(Element):
    pass

class p(Element):
    pass

class button(Element):
    pass
