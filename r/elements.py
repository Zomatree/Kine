from __future__ import annotations

from collections import UserString
from typing import TYPE_CHECKING, Any, Callable, TypedDict, cast

from typing_extensions import Self, Unpack

if TYPE_CHECKING:
    from .core import Node
    from .messages import ElementId
    from .scope import Scope

__all__ = (
    "Element",
    "div",
    "p",
    "button",
    "marquee",
    "String"
)

class ElementArgs(TypedDict, total=False):
    id: str
    cls: str

    onclick: Callable[[Any], None]

class Element:
    def __init__(self, scope: Scope, **attributes: Unpack[ElementArgs]):
        self.scope = scope
        self.children: tuple[Node[...], ...] = ()
        self.listeners: dict[str, Callable[[Any], None]] = {}

        self.parent_id: ElementId | None = None
        self.id = scope.scopes.next_element_id()

        for name, value in list(attributes.items()):
            if name.startswith("on"):
                self.listeners[name[2:]] = cast(Callable[[Any], None], value)
                del attributes[name]

        self.attributes = {k: str(v) for k, v in attributes.items()}

    def __getitem__(self, children: Node[...] | tuple[Node[...], ...]) -> Self:
        self.children = children if isinstance(children, tuple) else (children,)

        for child in self.children:
            if child:
                child.parent_id = self.id

        return self

class div(Element):
    pass

class p(Element):
    pass

class button(Element):
    pass

class marquee(Element):
    pass

class String(UserString):
    def __init__(self, scope: Scope, seq: object) -> None:
        super().__init__(seq)
        self.id = scope.scopes.next_element_id()
        self.parent_id: ElementId | None = None
