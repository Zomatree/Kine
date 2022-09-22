from __future__ import annotations
from collections import UserString

from typing import Callable, Concatenate, ParamSpec, TypeVar, Union

from .elements import Element
from .scope import ElementId, Scope, Scopes

__all__ = (
    "Component",
    "Node",
    "Nodes",
    "VString",
    "VElement",
    "VComponent",
    "VNode"
)

P = ParamSpec("P")
C_P = ParamSpec("C_P")
T = TypeVar("T")

Component = Callable[Concatenate[Scope, P], "Node"]
Node = Union[str, Element]
Nodes = list[Node]


class VString(UserString):
    __match_args__ = ("id", "data")

    def __init__(self, id: ElementId, value: str):
        self.id = id
        super().__init__(value)

class VElement:
    __match_args__ = ("id", "tag", "children", "attributes")

    def __init__(self, id: ElementId, tag: str, children: list[VNode], attributes: dict[str, str]):
        self.id = id
        self.tag = tag
        self.children = children
        self.attributes = attributes

class VComponent:
    __match_args__ = ("id", "name", "children")

    def __init__(self, id: ElementId, name: str, children: list[VNode]):
        self.id = id
        self.name = name
        self.children = children

VNode = Union[VString, VElement, VComponent]

def transform_node(scopes: Scopes, node: Node, id: ElementId = ElementId(0)) -> VNode:
    if isinstance(node, str):
        vnode = VString(id, node)
        id = ElementId(id + 1)
        return vnode

    elif isinstance(node, Element):
        nodes = []

        for child in node.children:
            nodes.append(transform_node(scopes, child, id))
            id = ElementId(id + 1)

        vnode = VElement(id, node.__class__.__name__, nodes, node.attributes)
        id = ElementId(id + 1)
        return vnode
