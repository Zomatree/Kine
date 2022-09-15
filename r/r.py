from __future__ import annotations

from typing import Callable, Concatenate, Generic, ParamSpec, TypeVar, Union

from .elements import Element
from .scope import Scope

__all__ = (
    "component",
    "Component",
    "Node",
    "Nodes"
)

P = ParamSpec("P")
C_P = ParamSpec("C_P")
T = TypeVar("T")

class ComponentFunction(Generic[P]):
    def __init__(self, func: Component[P]):
        self.func = func

    def __call__(self, cx: Scope, *args: P.args, **kwargs: P.kwargs) -> Node:
        nodes = self.func(cx, *args, **kwargs)
        return nodes

def component(func: Component[P]) -> ComponentFunction[P]:
    return ComponentFunction(func)

Component = Callable[Concatenate[Scope, P], "Node"]
Node = Union[str, Element, "Nodes"]
Nodes = list[Node]
