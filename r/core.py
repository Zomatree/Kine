from __future__ import annotations

import functools
from collections import UserString
from typing import (TYPE_CHECKING, Any, Callable, Concatenate, Generic,
                    ParamSpec, TypeVar, Union)

from .elements import Element

if TYPE_CHECKING:
    from .scope import Scope
    from .utils import ElementId, ScopeId

P = ParamSpec("P")
T = TypeVar("T")

__all__ = ("Listener", "VString", "VElement", "VNode", "ComponentFunction", "component", "Component", "Node", "Nodes")

class Listener:
    def __init__(self, name: str, func: Callable[[Any], None]):
        self.name = name
        self.func = func
        self.element_id: ElementId | None = None

class VString(UserString):
    def __init__(self, value: str):
        self.id: ElementId | None = None
        self.parent_id: ElementId | None = None
        self.key = None
        super().__init__(value)

class VElement:
    def __init__(self, tag: str, children: list[VNode], attributes: dict[str, Any], listeners: list[Listener]):
        self.id: ElementId | None = None
        self.parent_id: ElementId | None = None
        self.tag = tag
        self.children = children
        self.attributes = attributes
        self.listeners = listeners
        self.key = attributes.get("key")

class VPlaceholder:
    def __init__(self):
        self.id: ElementId | None = None
        self.parent_id: ElementId | None = None
        self.key = None

class VComponent:
    def __init__(self, func: ComponentFunction[...], parent_scope: ScopeId, key: str | None):
        self.parent_id: ElementId | None = None
        self.scope_id: ScopeId | None = None
        self.comp_func = func
        self.parent_scope = parent_scope
        self.key = key

VNode = Union[VString, VElement, VPlaceholder, VComponent]

class ComponentFunction(Generic[P]):
    def __init__(self, func: Callable[Concatenate[Scope, P], VNode], *args: P.args, **kwargs: P.kwargs):
        self.func = func
        self.id: ElementId | None = None
        self.scope_id: ScopeId | None = None
        self.parent_id: ElementId | None = None
        self._key: str | None = None
        self.args = args
        self.kwargs = kwargs

    def key(self, key: str):
        self._key = key
        return self

    def call(self, scope: Scope) -> VNode:
        return self.func(scope, *self.args, **self.kwargs)

def component(func: Callable[Concatenate[Scope, P], VNode]) -> Callable[Concatenate[P], ComponentFunction[P]]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        return ComponentFunction(func, *args, **kwargs)

    return wrapper

Component = Callable[Concatenate["Scope", P], "VNode"]
Node = Union[str, Element, ComponentFunction[P], None]
Nodes = list[Node[P]]
