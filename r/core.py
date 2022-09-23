from __future__ import annotations
from collections import UserString

from typing import Callable, Concatenate, Generic, ParamSpec, TypeVar, Union, cast

from .elements import Element
from .scope import ElementId, Scope, ScopeId, Scopes

P = ParamSpec("P")
C_P = ParamSpec("C_P")
T = TypeVar("T")

Component = Callable[Concatenate[Scope, P], "Node"]
Node = Union["String", Element, "ComponentFunction", None]
Nodes = list[Node]

class String(str):
    id: ElementId | None

    def __new__(cls, v):
        self = super().__new__(cls, v)
        self.id = None

        return self

class VString(UserString):
    def __init__(self, id: ElementId, value: str):
        self.id = id
        super().__init__(value)

class VElement:
    def __init__(self, id: ElementId, tag: str, children: list[VNode], attributes: dict[str, str], handlers: list[str]):
        self.id = id
        self.tag = tag
        self.children = children
        self.attributes = attributes
        self.handlers = handlers

VNode = Union[VString, VElement, None]

class ComponentFunction(Generic[P]):
    def __init__(self, func: Callable[Concatenate[Scope, P], Node]):
        self.func = cast(Callable[[Scope], Node], func)
        self.id: ElementId | None = None
        self.scope_id: ScopeId | None = None

        self.invoked = False
        self.args = ()
        self.kwargs = {}

    def __call__(self, *args: P.args, **kwargs: P.kwargs):
        self.invoked = True
        self.args = args
        self.kwargs = kwargs

        return self

    def _call(self, cx: Scope) -> Node:
        if not self.invoked:
            raise Exception

        return self.func(cx, *self.args, **self.kwargs)

def component(func: Callable[Concatenate[Scope, P], Node]) -> ComponentFunction[P]:
    return ComponentFunction(func)

def set_ids(scopes: Scopes, node: Node):
    if node and not node.id:
        node.id = scopes.next_element_id()

    if isinstance(node, Element):
        for child in node.children:
            set_ids(scopes, child)

# converts a Node into a VNode, presumes ids have already been set onto the nodes

def transform_node(scopes: Scopes, node: Node) -> VNode:
    if isinstance(node, String):
        assert node.id is not None

        vnode = VString(node.id, str(node))
        return vnode

    elif isinstance(node, Element):
        assert node.id is not None

        nodes = []

        for child in node.children:
            nodes.append(transform_node(scopes, child))

        vnode = VElement(
            node.id,
            node.__class__.__name__,
            nodes,
            node.attributes,
            list(node.handlers.keys())
        )

        return vnode

    elif isinstance(node, ComponentFunction):
        if not node.scope_id:
            node.scope_id = scopes.new_scope(None)  # todo: parent scope

        cx = scopes.get_scope(node.scope_id)

        child = node._call(cx)
        set_ids(scopes, child)

        return transform_node(scopes, child)
