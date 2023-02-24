from __future__ import annotations

from typing import Literal, overload, TypeVar, TYPE_CHECKING, cast

if TYPE_CHECKING:
    from ...renderers.web import WebVDom

from ... import Scope, messages

T = TypeVar("T")

class EvalMessage(messages.BaseEvent[Literal["EvalMessage"]]):
    code: str

class _Cookies(dict[str, str]):
    pass

class Cookies:
    def __init__(self, cx: Scope):
        self.cx = cx
        self.dom = cast("WebVDom", cx.scopes.dom)
        self.cookies = cx.root_scope().consume_context(_Cookies)

    @overload
    def get(self, name: str, default: None = None) -> str | None:
        ...

    @overload
    def get(self, name: str, default: T = ...) -> str | T:
        ...

    def get(self, name: str, default: T = None) -> str | T | None:
        return self.cookies.get(name, default)

    def set(self, name: str, value: str):
        self.cookies[name] = value

        msg = EvalMessage()
        msg.code = f"Cookies.set({repr(name)}, {repr(value)})"
        self.dom.custom_messages.put_nowait(msg)
        self.cx.schedule_update()

def use_cookies(cx: Scope) -> Cookies:
    return cx.use_hook(lambda: Cookies(cx))
