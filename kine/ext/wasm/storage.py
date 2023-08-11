from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, overload

from ...fullstack import IS_WEB_PLATFORM
from ... import Scope

if IS_WEB_PLATFORM or TYPE_CHECKING:
    import js

T = TypeVar("T")


class Storage:
    def __init__(self, cx: Scope, backing: js.Storage):
        self.cx = cx
        self.backing = backing

    @overload
    def get(self, name: str, default: T) -> str | T:
        ...

    @overload
    def get(self, name: str, default: None = ...) -> str | None:
        ...

    def get(self, name: str, default: T | None = None) -> str | None | T:
        return self.backing.getItem(name) or default

    def set(self, name: str, value: str):
        self.backing.setItem(name, value)
        self.cx.schedule_update()

    def remove(self, name: str):
        self.backing.removeItem(name)
        self.cx.schedule_update()

    def clear(self):
        self.backing.clear()
        self.cx.schedule_update()

    @overload
    def key(self, index: int, default: T) -> str | T:
        ...

    @overload
    def key(self, index: int, default: None = ...) -> str | None:
        ...

    def key(self, index: int, default: T | None = None) -> str | None | T:
        return self.backing.key(index) or default

    def __len__(self) -> int:
        return self.backing.length

    def __getitem__(self, key: str) -> str:
        value = self.get(key)

        if value is None:
            raise IndexError

        return value

    def __setitem__(self, key: str, value: str):
        self.set(key, value)


def use_local_storage(cx: Scope) -> Storage:
    import js

    return cx.use_hook(lambda: Storage(cx, js.window.localStorage))


def use_session_storage(cx: Scope) -> Storage:
    import js

    return cx.use_hook(lambda: Storage(cx, js.window.sessionStorage))
