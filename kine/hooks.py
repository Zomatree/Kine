from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Coroutine, Generic, TypeVar

from kine.messages import Immediate

from .utils import ScopeId

if TYPE_CHECKING:
    from .scope import Scope


__all__ = (
    "use_state",
    "use_future",
    "UseState",
    "UseFuture",
    "signal",
    "Signal",
    "use_read_signal",
    "use_write_signal",
    "use_peek_signal",
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

    def __repr__(self) -> str:
        return f"<UseState value={self.value!r}>"

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

@dataclass
class InnerSignal(Generic[T]):
    value: T
    readers: list[ScopeId] = field(default_factory=list)

class Signal(Generic[T]):
    def __init__(self, initial: Callable[[], T]):
        self.initial = initial
        self.instances: dict[int, InnerSignal[T]] = {}

    def requires_update(self, cx: Scope):
        for scope_id in self.instances[cx.root_id].readers:
            cx.scopes.dom.messages.put_nowait(Immediate(scope_id))

    def mutate(self, cx: Scope, f: Callable[[T], Any]):
        inner = write_hook(cx, self)

        f(inner.value)

        self.requires_update(cx)

    def modify(self, cx: Scope, f: Callable[[T], T]):
        inner = write_hook(cx, self)

        inner.value = f(inner.value)

        self.requires_update(cx)

    def __repr__(self) -> str:
        return f"<Signal initial_value={self.initial()!r}>"

def signal(initial: Callable[[], T]) -> Signal[T]:
    return Signal(initial)


def read_hook(cx: Scope, signal: Signal[Any]):
    if not (inner := signal.instances.get(cx.root_id)):
        inner = signal.instances[cx.root_id] = InnerSignal(signal.initial())

    inner.readers.append(cx.scope_id)
    return inner

def use_read_signal(cx: Scope, signal: Signal[T]) -> T:
    inner = cx.use_hook(read_hook, cx, signal)
    return inner.value


def write_hook(cx: Scope, signal: Signal[T]) -> InnerSignal[T]:
    if not (inner := signal.instances.get(cx.root_id)):
        inner = signal.instances[cx.root_id] = InnerSignal(signal.initial())

    return inner

def use_write_signal(cx: Scope, signal: Signal[T]) -> Callable[[T], None]:
    inner = cx.use_hook(write_hook, cx, signal)

    def writer(value: T):
        inner.value = value
        signal.requires_update(cx)

    return writer

def use_peek_signal(cx: Scope, signal: Signal[T]) -> T:
    inner = cx.use_hook(write_hook, cx, signal)

    return inner.value
