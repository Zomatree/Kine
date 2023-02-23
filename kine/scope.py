from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Coroutine, Optional, TypeVar

from .core import ComponentFunction, Element, Listener, VComponent, VElement, VNode, VPlaceholder, VString
from .messages import EventMessage, Immediate
from .elements import Element
from .utils import ElementId, ScopeId, TaskId

if TYPE_CHECKING:
    from .core import Node
    from .dom import VirtualDom

__all__ = ("Scope", "Scopes", "TaskQueue")

T = TypeVar("T")


class Scope:
    def __init__(
        self, scope_id: ScopeId, parent_scope: Optional[Scope], height: int, container: ElementId, scopes: Scopes
    ):
        self.scope_id = scope_id
        self.parent_scope = parent_scope
        self.component: ComponentFunction[...] | None = None
        self.height = height
        self.container = container
        self.scopes = scopes
        self.contexts: dict[Any, Any] = {}
        self.generation = 0
        self.frame_0 = VString("placeholder")
        self.frame_1 = VString("placeholder")
        self.hooks: list[Any] = []
        self.hook_idx = 0
        self.children: tuple[Node, ...] = ()

    def use_hook(self: Scope, f: Callable[[], T]) -> T:
        hook_len = len(self.hooks)

        if self.hook_idx >= hook_len:
            self.hooks.append(f())

        value = self.hooks[self.hook_idx]
        self.hook_idx += 1

        return value

    def provide_context(self, context: T) -> T:
        # lets just hope users dont use specialforms

        self.contexts[type(context)] = context

        return context

    def consume_context(self, context_t: type[T]) -> T:
        try:
            return self.contexts[context_t]
        except KeyError:
            parent_scope = self.parent_scope

            while parent_scope:
                try:
                    return parent_scope.contexts[context_t]
                except KeyError:
                    parent_scope = parent_scope.parent_scope

            raise KeyError from None

    def provide_root_context(self, context: T) -> T:
        return self.root_scope().provide_context(context)

    def root_scope(self) -> Scope:
        scope = self

        while parent := scope.parent_scope:
            scope = parent

        return scope

    def schedule_update(self):
        self.scopes.dom.messages.put_nowait(Immediate(self.scope_id))

    def wip_frame(self) -> VNode:
        if self.generation & 1 == 0:
            return self.frame_0
        else:
            return self.frame_1

    def fin_frame(self) -> VNode:
        if self.generation & 1 == 1:
            return self.frame_0
        else:
            return self.frame_1

    def set_wip_frame(self, node: VNode):
        if self.generation & 1 == 0:
            self.frame_0 = node
        else:
            self.frame_1 = node

    def set_fin_frame(self, node: VNode):
        if self.generation & 1 == 1:
            self.frame_0 = node
        else:
            self.frame_1 = node

    def next_frame(self):
        self.generation += 1

    def render(self, node: Node) -> VNode:
        if isinstance(node, str):
            vnode = VString(node)
            return vnode

        elif isinstance(node, Element):
            nodes: list[VNode] = []

            vnode = VElement(
                node.__class__.__name__,
                nodes,
                node.attributes,  # type: ignore
                [Listener(name, func) for name, func in node.listeners.items()],
                node._key,
            )

            for child in node.children:
                nodes.append(self.render(child))

            return vnode

        elif isinstance(node, ComponentFunction):
            return VComponent(node, self.scope_id, node._key)

        elif node is None:
            return VPlaceholder()

    def spawn(self, coro: Coroutine[Any, Any, T]) -> asyncio.Task[T]:
        task = asyncio.create_task(coro)
        self.scopes.tasks.spawn(self.scope_id, task)

        return task

    def _reset(self):
        self.hook_idx = 0
        self.parent_scope = None
        self.generation = 0
        self.contexts.clear()


class Scopes:
    dom: VirtualDom

    def __init__(self, app: ComponentFunction[...]):
        self.scopes: dict[ScopeId, Scope] = {}
        self.scope_id = ScopeId(0)
        self.element_id = ElementId(0)
        self.tasks = TaskQueue()
        self.element_idx = 0
        self.root = VElement("div", [], {}, [], None)
        self.nodes: dict[ElementId, VNode] = {}
        self.root.id = self.reserve_node(self.root)

        scope_id = self.new_scope(None, ElementId(0))
        scope = self.get_scope(scope_id)
        scope.component = app

    def new_scope(self, parent: Optional[ScopeId], container: ElementId) -> ScopeId:
        scope_id = self.scope_id
        self.scope_id += 1

        parent_scope = self.scopes[parent] if parent is not None else None
        height = parent_scope.height + 1 if parent_scope else 0

        scope = Scope(scope_id, parent_scope, height, container, self)

        self.scopes[scope_id] = scope

        return scope_id

    def remove_scope(self, id: ScopeId) -> Scope:
        return self.scopes.pop(id)

    def get_scope(self, scope_id: ScopeId) -> Scope:
        return self.scopes[scope_id]

    def next_element_id(self) -> ElementId:
        id = self.element_id
        self.element_id = ElementId(self.element_id + 1)

        return id

    def update_node(self, node: VNode, id: ElementId):
        self.nodes[id] = node

    def remove_node(self, id: ElementId):
        del self.nodes[id]

    def reserve_node(self, node: VNode) -> ElementId:
        id = ElementId(self.element_idx)
        self.nodes[id] = node
        self.element_idx += 1
        return id

    def call_listener_with_bubbling(self, event: EventMessage):
        element_id = event.element_id

        while element_id:
            node = self.nodes[element_id]

            if isinstance(node, VElement):
                for listener in node.listeners:
                    if listener.name == event.name:
                        listener.func(event.data)

            element_id = node.parent_id

    def run_scope(self, scope_id: ScopeId):
        scope = self.get_scope(scope_id)
        scope.hook_idx = 0

        assert scope.component is not None

        scope.children = scope.component.children

        if node := scope.component.call(scope):
            scope.set_wip_frame(node)
        else:
            scope.set_wip_frame(VPlaceholder())

        scope.next_frame()


class TaskQueue:
    def __init__(self):
        self.tasks: dict[TaskId, asyncio.Task[Any]] = {}
        self.task_map: dict[ScopeId, set[TaskId]] = {}
        self.current_task_id = 0

    def spawn(self, scope_id: ScopeId, task: asyncio.Task[Any]) -> TaskId:
        task_id = TaskId((self.current_task_id, scope_id))
        self.current_task_id += 1

        self.tasks[task_id] = task
        self.task_map.setdefault(scope_id, set()).add(task_id)

        return task_id

    def remove(self, task_id: TaskId):
        del self.tasks[task_id]

        if tasks := self.task_map.get(task_id[1]):
            tasks.remove(task_id)
