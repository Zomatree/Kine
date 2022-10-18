from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar, cast

from .core import (ComponentFunction, Element, Listener, VElement, VNode,
                   VString)
from .dom import EventMessage, Immediate
from .elements import Element, String
from .utils import ElementId, ScopeId, TaskId

if TYPE_CHECKING:
    from .core import Node, P, VNode
    from .dom import VirtualDom

__all__ = ("Scope", "Scopes", "TaskQueue")

T = TypeVar("T")


class Scope:
    def __init__(self, scope_id: ScopeId, parent_scope: Optional[Scope], height: int, container: ElementId, scopes: Scopes):
        self.scope_id = scope_id
        self.parent_scope = parent_scope
        self.component: ComponentFunction[...] | None = None
        self.height = height
        self.container = container
        self.scopes = scopes
        self.contexts: dict[Any, Any] = {}
        self.generation = 0
        self.frames: tuple[Optional[VNode], Optional[VNode]] = (None, None)
        self.hooks: list[Any] = []
        self.hook_idx = 0

    def use_hook(self: Scope, f: Callable[[], T]) -> T:
        hook_len = len(self.hooks)

        if self.hook_idx >= hook_len:
            self.hooks.append(f())

        value = self.hooks[self.hook_idx]
        self.hook_idx += 1

        return value

    def provide_context(self, value: T) -> T:
        # lets just hope users dont use specialforms

        self.contexts[type(value)] = value

        return value

    def consume_context(self, value_t: type[T]) -> T:
        try:
            return self.contexts[value_t]
        except IndexError:
            parent_scope = self.parent_scope

            while parent_scope:
                try:
                    return parent_scope.contexts[value_t]
                except IndexError:
                    parent_scope = parent_scope.parent_scope

            raise IndexError from None

    def schedule_update(self):
        self.scopes.dom.messages.put_nowait(Immediate(self.scope_id))

    def wip_frame(self) -> VNode:
        if self.generation & 1 == 0:
            return cast(VNode, self.frames[0])
        else:
            return cast(VNode, self.frames[1])

    def fin_frame(self) -> VNode:
        if self.generation & 1 == 1:
            return cast(VNode, self.frames[0])
        else:
            return cast(VNode, self.frames[1])

    def set_wip_frame(self, node: VNode):
        if self.generation & 1 == 0:
            self.frames = (node, self.frames[0])
        else:
            self.frames = (self.frames[1], node)

    def set_fin_frame(self, node: VNode):
        if self.generation & 1 == 1:
            self.frames = (node, self.frames[0])
        else:
            self.frames = (self.frames[1], node)

    def next_frame(self):
        self.generation += 1

    def render(self, node: Node[P]) -> VNode:
        if isinstance(node, String):
            vnode = VString(node.id, node.parent_id, str(node))
            return vnode

        elif isinstance(node, Element):
            assert node.id is not None

            nodes: list[VNode] = []

            vnode = VElement(
                node.id,
                node.parent_id,
                node.__class__.__name__,
                nodes,
                node.attributes,
                [Listener(name, func, node.id) for name, func in node.listeners.items()]
            )

            for child in node.children:
                nodes.append(self.render(child))

            return vnode

        elif isinstance(node, ComponentFunction):
            return node.call()
        elif node is 
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
        self.root = VElement(self.next_element_id(), None, "div", [], {}, [])
        self.nodes: dict[ElementId, VNode] = {self.root.id: self.root}

        scope_id = self.new_scope(None, ElementId(0))
        scope = self.get_scope(scope_id)
        scope.component = app(scope)

    def new_scope(self, parent: Optional[ScopeId], container: ElementId) -> ScopeId:
        scope_id = self.scope_id
        self.scope_id += 1

        height = parent + 1 if parent else 0
        parent_scope = self.scopes[parent] if parent else None

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

    def call_listener_with_bubbling(self, event: EventMessage):
        print(event)
        element_id = event.element_id

        while element_id := element_id:
            element = self.nodes[element_id]

            if not element:
                break

            if isinstance(element, VElement):
                for listener in element.listeners:
                    if listener.name == event.name:
                        listener.func(event.data)

            element_id = element.parent_id

    def run_scope(self, scope_id: ScopeId):
        scope = self.get_scope(scope_id)
        scope.hook_idx = 0

        if not scope.component:
            raise

        if node := scope.component.call():
            scope.set_wip_frame(node)
        else:
            scope.set_wip_frame(None)

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
