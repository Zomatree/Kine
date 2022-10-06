from __future__ import annotations
from collections import UserString

from typing import Any, Callable, Concatenate, Generic, ParamSpec, TypeVar, Union, cast

from .elements import Element
from .scope import ElementId, Scope, ScopeId, Scopes

P = ParamSpec("P")
C_P = ParamSpec("C_P")
T = TypeVar("T")

Component = Callable[Concatenate[Scope, P], "Node[P]"]
Node = Union["String", Element, "ComponentFunction[P]", None]
Nodes = list[Node[P]]

class Listener:
    def __init__(self, name: str, func: Callable[[Any], None], element_id: ElementId):
        self.name = name
        self.func = func
        self.element_id = element_id

class String(str):
    id: ElementId | None
    parent_id: ElementId | None

    def __new__(cls, v: Any):
        self = super().__new__(cls, v)
        self.id = None
        self.parent_id = None

        return self

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

VNode = Union[VString, VElement, None]

class ComponentFunction(Generic[P]):
    def __init__(self, func: Callable[Concatenate[Scope, P], Node[Any]]):
        self.func = cast(Callable[[Scope], Node[Any]], func)
        self.id: ElementId | None = None
        self.scope_id: ScopeId | None = None
        self.parent_id: ElementId | None = None

        self.invoked = False
        self.args: tuple[Any, ...] = ()
        self.kwargs: dict[Any, Any] = {}

    def __call__(self, *args: P.args, **kwargs: P.kwargs):
        self.invoked = True
        self.args = args
        self.kwargs = kwargs

        return self

    def _call(self, cx: Scope) -> Node[P]:
        if not self.invoked:
            raise Exception

        return self.func(cx, *self.args, **self.kwargs)

def component(func: Callable[Concatenate[Scope, P], Node[C_P]]) -> ComponentFunction[P]:
    return ComponentFunction(func)

def set_ids(scopes: Scopes, node: Node[P], parent_id: ElementId | None = None):
    if node and not node.id:
        node.id = scopes.next_element_id()

    if isinstance(node, String):
        node.parent_id = parent_id

    if isinstance(node, Element):
        node.parent_id = parent_id

        for child in node.children:
            set_ids(scopes, child, node.id)

# converts a Node into a VNode, presumes ids have already been set onto the nodes

def transform_node(scopes: Scopes, node: Node) -> VNode:
    if isinstance(node, String):
        assert node.id is not None

        vnode = VString(node.id, None, str(node))
        return vnode

    elif isinstance(node, Element):
        assert node.id is not None

        nodes = []

        for child in node.children:
            nodes.append(transform_node(scopes, child))

        vnode = VElement(
            node.id,
            node.parent_id,
            node.__class__.__name__,
            nodes,
            node.attributes,
            [Listener(name, func, node.id) for name, func in node.listeners.items()]
        )

        return vnode

    elif isinstance(node, ComponentFunction):
        if not node.scope_id:
            node.scope_id = scopes.new_scope(None)  # todo: parent scope

        cx = scopes.get_scope(node.scope_id)

        child = node._call(cx)
        set_ids(scopes, child)

        return transform_node(scopes, child)
