from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Coroutine, ParamSpec, TypeVar

from .core import ComponentFunction, Listener, VComponent, VElement, VNode, VPlaceholder, VString
from .elements import Element
from .messages import EventMessage, Immediate
from .utils import ROOT_ELEMENT, ROOT_SCOPE, ElementId, ScopeId, TaskId
from .extras import _ErrorBoundary

if TYPE_CHECKING:
    from .core import Node
    from .dom import VirtualDom

__all__ = ("Scope", "Scopes", "TaskQueue")

P = ParamSpec("P")
T = TypeVar("T")


class Scope:
    def __init__(
        self, root_id: int, scope_id: ScopeId, parent_scope: Scope | None, height: int, container: ElementId, scopes: Scopes
    ):
        self.root_id = root_id
        self.scope_id: ScopeId = scope_id
        self.parent_scope = parent_scope
        self.component: ComponentFunction[...] | None = None
        self.height = height
        self.container = container
        self.scopes = scopes
        self.contexts: dict[Any, Any] = {}
        self.generation = 0
        self.frame_0: tuple[VNode, tuple[Any, ...], dict[str, Any]] = (VPlaceholder(), (), {})
        self.frame_1: tuple[VNode, tuple[Any, ...], dict[str, Any]] = (VPlaceholder(), (), {})
        self.hooks: list[Any] = []
        self.hook_idx = 0
        self.children: tuple[Node, ...] = ()
        self.has_errored: bool = False

    def use_hook(self, f: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
        hook_len = len(self.hooks)

        if self.hook_idx >= hook_len:
            self.hooks.append(f(*args, **kwargs))

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

            raise LookupError from None

    def provide_root_context(self, context: T) -> T:
        return self.root_scope().provide_context(context)

    def root_scope(self) -> Scope:
        scope = self

        while parent := scope.parent_scope:
            scope = parent

        return scope

    def schedule_update(self):
        self.scopes.dom.messages.put_nowait(Immediate(self.scope_id))

    def wip_frame(self) -> tuple[VNode, tuple[Any, ...], dict[str, Any]]:
        if self.generation & 1 == 0:
            return self.frame_0

        return self.frame_1

    def fin_frame(self) -> tuple[VNode, tuple[Any, ...], dict[str, Any]]:
        if self.generation & 1 == 1:
            return self.frame_0

        return self.frame_1

    def set_wip_frame(self, node: VNode, args: tuple[Any, ...], kwargs: dict[str, Any]):
        if self.generation & 1 == 0:
            self.frame_0 = (node, args, kwargs)
        else:
            self.frame_1 = (node, args, kwargs)

    def set_fin_frame(self, node: VNode, args: tuple[Any, ...], kwargs: dict[str, Any]):
        if self.generation & 1 == 1:
            self.frame_0 = (node, args, kwargs)
        else:
            self.frame_1 = (node, args, kwargs)

    def next_frame(self):
        self.generation += 1

    def render(self, node: Node) -> VNode:
        if isinstance(node, str):
            return VString(node)

        elif isinstance(node, Element):
            nodes: list[VNode] = []

            vnode = VElement(
                node.name,
                nodes,
                node.attributes,  # type: ignore - cant downcast to dict
                [Listener(name, func) for name, func in node.listeners.items()],
                node._key,
                node.ref
            )

            nodes.extend([self.render(child) for child in node.children])

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
    def __init__(self, app: ComponentFunction[...], dom: VirtualDom):
        self.dom = dom
        self.scopes: dict[ScopeId, Scope] = {}
        self.scope_id = ROOT_SCOPE
        self.element_id = ROOT_ELEMENT
        self.tasks = TaskQueue()
        self.element_idx = 0
        self.root = VElement("div", [], {}, [], None, None)
        self.nodes: dict[ElementId, VNode] = {}
        self.root.id = self.reserve_node(self.root)

        scope_id = self.new_scope(None, ROOT_ELEMENT)
        scope = self.get_scope(scope_id)
        scope.component = app

    def new_scope(self, parent: ScopeId | None, container: ElementId) -> ScopeId:
        scope_id = self.scope_id
        self.scope_id += 1

        parent_scope = self.scopes[parent] if parent is not None else None
        height = parent_scope.height + 1 if parent_scope else 0

        scope = Scope(id(self), scope_id, parent_scope, height, container, self)

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
                        try:
                            listener.func(event.data)
                        except Exception as e:
                            if current_scope := node.scope_id:
                                scope = self.get_scope(current_scope)
                                
                                try:
                                    boundary = scope.consume_context(_ErrorBoundary)
                                except LookupError:
                                    raise e
                                
                                scope.has_errored = True
                                node = scope.render(boundary.fallback(e).call(scope))
                                scope.set_wip_frame(node, (e,), {})
                                
                                scope.schedule_update()
                                
                                break
                        
                        if not event.bubbles:
                            break

            element_id = node.parent_id

    def run_scope(self, scope_id: ScopeId):
        scope = self.get_scope(scope_id)
        scope.hook_idx = 0

        component = scope.component
        assert component is not None

        scope.children = component.children
        
        if not scope.has_errored:
            try:
                if scope.generation != 0 and component.memorize:
                    finished_node, args, kwargs = scope.fin_frame()

                    if args == component.args and kwargs == component.kwargs and not scope.hooks:
                        node = finished_node
                    else:
                        node = scope.render(component.call(scope))
                else:
                    node = scope.render(component.call(scope))
            except Exception as e:
                try:
                    boundary = scope.consume_context(_ErrorBoundary)
                except LookupError:
                    raise e

                scope.has_errored = True
                node = scope.render(boundary.fallback(e).call(scope))

            scope.set_wip_frame(node, component.args, component.kwargs)

        scope.has_errored = False
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
