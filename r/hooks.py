from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Coroutine, Generic, TypeVar

if TYPE_CHECKING:
    from .scope import Scope


__all__ = ("use_state", "use_future", "UseState")

T = TypeVar("T")

def use_state(cx: Scope, func: Callable[[], T]) -> UseState[T]:
    return cx.use_hook(lambda: UseState[T](cx, cx.hook_idx, func()))

def use_future(cx: Scope, func: Callable[[], Coroutine[Any, Any, T]]) -> T | None:
    def hook():
        state = UseFuture[T](cx, cx.hook_idx)
        task = asyncio.create_task(func())

        def cb(task: asyncio.Task[T]):
            state.value = task.result()
            cx.scopes.dom.dirty_scopes.add(cx.scope_id)

        task.add_done_callback(cb)

        cx.scopes.tasks.spawn(cx.scope_id, task)

        return state

    return cx.use_hook(hook).value

class UseState(Generic[T]):
    def __init__(self, scope: Scope, idx: int, value: T):
        self.scope = scope
        self.idx = idx
        self.value = value

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        self.value = value
        self.scope.schedule_update()

    def modify(self, func: Callable[[T], T]):
        self.set(func(self.get()))

class UseFuture(Generic[T]):
    def __init__(self, scope: Scope, idx: int):
        self.scope = scope
        self.idx = idx
        self.value: T | None = None
