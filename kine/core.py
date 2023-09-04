from __future__ import annotations

import functools
from collections import UserString
from typing import TYPE_CHECKING, Any, Callable, Concatenate, Generator, Generic, ParamSpec, TypeAlias, TypeVar, Union

from .elements import Element

if TYPE_CHECKING:
    from .scope import Scope
    from .utils import ElementId, ScopeId
    from .hooks import UseRef

P = ParamSpec("P")
T = TypeVar("T")

__all__ = ("Listener", "VString", "VElement", "VNode", "ComponentFunction", "component", "Component", "Node", "Nodes", "memo")


class Listener:
    def __init__(self, name: str, func: Callable[[Any], None]):
        self.name = name
        self.func = func
        self.element_id: ElementId | None = None

    def __repr__(self) -> str:
        return f"<Listener name={self.name!r} func={self.func!r} element_id={self.element_id!r}>"

class VString(UserString):
    def __init__(self, value: str):
        self.id: ElementId | None = None
        self.parent_id: ElementId | None = None
        self.key = None
        super().__init__(value)

    def __repr__(self) -> str:
        return f"<VString id={self.id!r} data={super().__repr__()}>"

class VElement:
    def __init__(
        self, tag: str, children: list[VNode], attributes: dict[str, Any], listeners: list[Listener], key: str | None, ref: UseRef[Any] | None
    ):
        self.id: ElementId | None = None
        self.parent_id: ElementId | None = None
        self.tag = tag
        self.children = children
        self.attributes = attributes
        self.listeners = listeners
        self.key = key
        self.ref = ref

    def __repr__(self) -> str:
        return f"<VElement id={self.id!r} tag={self.tag!r} children={self.children!r}>"

class VPlaceholder:
    def __init__(self):
        self.id: ElementId | None = None
        self.parent_id: ElementId | None = None
        self.key = None

    def __repr__(self) -> str:
        return f"<VPlaceholder id={self.id!r}>"


class VComponent:
    def __init__(self, func: ComponentFunction[...], parent_scope: ScopeId, key: str | None):
        self.parent_id: ElementId | None = None
        self.scope_id: ScopeId | None = None
        self.func = func
        self.parent_scope = parent_scope
        self.key = key

    def __repr__(self) -> str:
        return f"<VComponent scope_id={self.scope_id!r} func={self.func!r}>"

VNode: TypeAlias = Union[VString, VElement, VPlaceholder, VComponent]


class ComponentFunction(Generic[P]):
    def __init__(self, func: Callable[Concatenate[Scope, P], VNode], *args: P.args, **kwargs: P.kwargs):
        self.func = func
        self.children: tuple[Node, ...] = ()
        self.id: ElementId | None = None
        self.scope_id: ScopeId | None = None
        self.parent_id: ElementId | None = None
        self._key: str | None = None
        self.args = args
        self.kwargs = kwargs
        self.memorize: bool = False

    def key(self, key: str):
        self._key = key
        return self

    def call(self, scope: Scope) -> VNode:
        return self.func(scope, *self.args, **self.kwargs)

    def __getitem__(self, children: Node | tuple[Node, ...] | Generator[Node, Any, Any]):
        if isinstance(children, Generator):
            children = tuple(children)
        elif isinstance(children, tuple):
            pass
        else:
            children = (children,)

        self.children = children
        return self


def component(func: Callable[Concatenate[Scope, P], VNode]) -> Callable[P, ComponentFunction[P]]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        return ComponentFunction(func, *args, **kwargs)

    return wrapper

def memo(func: Callable[P, ComponentFunction[P]]) -> Callable[P, ComponentFunction[P]]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        component = func(*args, **kwargs)
        component.memorize = True
        return component

    return wrapper

Component: TypeAlias = Callable[Concatenate["Scope", P], "VNode"]
Node: TypeAlias = Union[str, Element, ComponentFunction[...], None]
Nodes: TypeAlias = list[Node]
