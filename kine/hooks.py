from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Coroutine, Generic, TypeVar

if TYPE_CHECKING:
    from .scope import Scope


__all__ = (
    "use_state",
    "use_future",
    "UseState",
    "UseFuture",
    "GlobalState",
    "GlobalStateCallback",
    "use_global_state",
    "use_set",
    "use_read",
)

T = TypeVar("T")


def use_state(cx: Scope, func: Callable[[], T]) -> UseState[T]:
    return cx.use_hook(lambda: UseState[T](cx, cx.hook_idx, func()))


def use_future(cx: Scope, func: Callable[[], Coroutine[Any, Any, T]]) -> UseFuture[T]:
    def hook():
        state = UseFuture[T](cx, cx.hook_idx, func)

        return state

    return cx.use_hook(hook)


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

    def mutate(self, func: Callable[[T], None]):
        value = self.value
        func(value)
        self.set(value)


class UseFuture(Generic[T]):
    def __init__(self, scope: Scope, idx: int, func: Callable[[], Coroutine[Any, Any, T]]):
        self.scope = scope
        self.idx = idx
        self.value: T | None = None
        self.func = func
        self.task = self.restart()

    def restart(self) -> asyncio.Task[T]:
        task = self.scope.spawn(self.func())

        def cb(task: asyncio.Task[T]):
            self.value = task.result()
            self.scope.scopes.dom.dirty_scopes.add(self.scope.scope_id)

        task.add_done_callback(cb)

        return task

GlobalStateCallback = Callable[[], T]


class GlobalState:
    def __init__(self, scope: Scope):
        self.scope = scope
        self.states: dict[GlobalStateCallback[Any], Any] = {}

    def get(self, state: GlobalStateCallback[T]) -> T:
        if state in self.states:
            return self.states[state]
        else:
            value = self.states[state] = state()
            return value


def use_global_state(cx: Scope) -> GlobalState:
    def hook():
        try:
            return cx.consume_context(GlobalState)
        except:
            return cx.provide_root_context(GlobalState(cx))

    return cx.use_hook(hook)


def use_read(cx: Scope, state: GlobalStateCallback[T]) -> T:
    root = use_global_state(cx)
    value = root.get(state)

    return value


def use_set(cx: Scope, state: GlobalStateCallback[T]) -> Callable[[T], None]:
    root = use_global_state(cx)

    def callback(value: T):
        root.states[state] = value

        cx.schedule_update()

    return callback
