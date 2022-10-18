from __future__ import annotations

from collections import UserString
from typing import (TYPE_CHECKING, Any, Callable, Concatenate, Generic,
                    ParamSpec, TypeVar, Union, cast)

from .elements import Element, String

if TYPE_CHECKING:
    from .scope import Scope
    from .utils import ElementId, ScopeId

P = ParamSpec("P")
T = TypeVar("T")

__all__ = ("Listener", "VString", "VElement", "VNode", "ComponentFunction", "component", "Component", "Node", "Nodes")

class Listener:
    def __init__(self, name: str, func: Callable[[Any], None], element_id: ElementId):
        self.name = name
        self.func = func
        self.element_id = element_id

class VString(UserString):
    def __init__(self, id: ElementId, parent_id: ElementId | None, value: str):
        self.id = id
        self.parent_id = parent_id
        super().__init__(value)

class VElement:
    def __init__(self, id: ElementId, parent_id: ElementId | None, tag: str, children: list[VNode], attributes: dict[str, str], listeners: list[Listener]):
        self.id = id
        self.parent_id = parent_id
        self.tag = tag
        self.children = children
        self.attributes = attributes
        self.listeners = listeners

class VPlaceholder:
    def __init__(self, id: ElementId, parent_id: ElementId | None):
        self.id = id
        self.parent_id = parent_id

VNode = Union[VString, VElement, VPlaceholder]

class ComponentFunction(Generic[P]):
    def __init__(self, func: Callable[Concatenate[Scope, P], VNode]):
        self.func = cast("Callable[[Scope], VNode]", func)
        self.scope: Scope | None = None
        self.id: ElementId | None = None
        self.scope_id: ScopeId | None = None
        self.parent_id: ElementId | None = None

        self.invoked = False
        self.args: tuple[Any, ...] = ()
        self.kwargs: dict[Any, Any] = {}

    def __call__(self, scope: Scope, *args: P.args, **kwargs: P.kwargs):
        self.invoked = True

        self.scope = scope
        self.scope.component = self

        self.args = args
        self.kwargs = kwargs

        return self

    def call(self) -> VNode:
        if not self.invoked:
            raise Exception

        return self.func(cast("Scope", self.scope), *self.args, **self.kwargs)

def component(func: Callable[Concatenate[Scope, P], VNode]) -> ComponentFunction[P]:
    return ComponentFunction(func)


Component = Callable[Concatenate["Scope", P], "VNode"]
Node = Union[String, Element, ComponentFunction[P], None]
Nodes = list[Node[P]]
