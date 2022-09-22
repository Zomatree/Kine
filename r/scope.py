from __future__ import annotations

from typing import Any, Callable, Coroutine, NewType, Optional, TypeVar, cast
import asyncio

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")

ScopeId = NewType("ScopeId", int)
TaskId = NewType("TaskId", tuple[int, ScopeId])
ElementId = NewType("ElementId", int)

class Scope:
    def __init__(self, scope_id: ScopeId, parent_scope: Optional[Scope], height: int, scopes: Scopes):
        self.scope_id = scope_id
        self.parent_scope = parent_scope
        self.height = height
        self.scopes = scopes
        self.contexts = {}

        self.hooks: list[Any] = []
        self.hook_idx = 0
        self.tasks = TaskQueue()

    def use_hook(self, f: Callable[[], T]) -> T:
        hook_len = len(self.hooks)

        if self.hook_idx >= hook_len:
            print("Calling hook")
            self.hooks.append(f())

        value = self.hooks[self.hook_idx]
        self.hook_idx += 1

        return value

    def use_state(self, value: T) -> tuple[Callable[[T], None], T]:
        value = self.use_hook(lambda: value)
        idx = self.hook_idx - 1

        def update(value: T):
            self.hooks[idx] = value
            self.schedule_update()

        return (update, value)

    def use_future(self, coro: Coroutine[Any, Any, T]) -> T | None:
        def hook():
            task = asyncio.create_task(coro)
            self.tasks.spawn(self.scope_id, task)

            (set_result, _) = self.use_state(cast(None | T, None))

            task.add_done_callback(lambda t: set_result(t.result()))
            return self.hook_idx - 1

        idx = self.use_hook(hook)

        return self.hooks[idx]

    def provide_context(self, value: T, ty: type[T] | None = None):
        if not ty:
            ty = type(value)

        self.contexts[ty] = value

        return value

    def consume_context(self, value_t: type[T]) -> T:
        return self.contexts[value_t]

    def schedule_update(self):
        ...

    def _reset(self):
        self.hook_idx = 0

    def next_scope(self) -> Scope:
        return self.scopes.new_scope(self.scope_id)

class Scopes:
    def __init__(self):
        self.scopes: dict[ScopeId, Scope] = {}
        self.scope_id = ScopeId(0)

    def new_scope(self, parent: Optional[ScopeId]) -> Scope:
        scope_id = self.scope_id
        self.scope_id += 1

        height = parent + 1 if parent else 0
        parent_scope = self.scopes[parent] if parent else None

        scope = Scope(scope_id, parent_scope, height, self)

        self.scopes[scope_id] = scope

        return scope

    def remove_scope(self, id: int):
        ...


class TaskQueue:
    def __init__(self):
        self.tasks: dict[TaskId, asyncio.Task] = {}
        self.task_map: dict[ScopeId, set[TaskId]] = {}
        self.current_task_id = 0

    def spawn(self, scope_id: ScopeId, task: asyncio.Task) -> TaskId:
        task_id = TaskId((self.current_task_id, scope_id))
        self.current_task_id += 1

        self.tasks[task_id] = task
        self.task_map.setdefault(scope_id, set()).add(task_id)

        return task_id

    def remove(self, task_id: TaskId):
        del self.tasks[task_id]

        if tasks := self.task_map.get(task_id[1]):
            tasks.remove(task_id)
