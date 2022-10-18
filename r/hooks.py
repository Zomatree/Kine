from __future__ import annotations

import asyncio
from typing import (TYPE_CHECKING, Any, Callable, Coroutine, Generic, TypeVar,
                    cast)

if TYPE_CHECKING:
    from .scope import Scope


__all__ = ("use_state", "use_future", "UseState")

T = TypeVar("T")

def use_state(cx: Scope, value: T) -> UseState[T]:
    return cx.use_hook(lambda: UseState[T](cx, cx.hook_idx, value))

def use_future(cx: Scope, coro: Coroutine[Any, Any, T]) -> T | None:
    def hook():
        task = asyncio.create_task(coro)
        cx.scopes.tasks.spawn(cx.scope_id, task)

        result = use_state(cx, cast(None | T, None))

        task.add_done_callback(lambda t: result.set(t.result()))
        return cx.hook_idx - 1

    idx = cx.use_hook(hook)

    return cx.hooks[idx]

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
