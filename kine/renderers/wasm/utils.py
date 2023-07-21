from __future__ import annotations

import asyncio
from enum import Enum
import json
from typing import TYPE_CHECKING, Any, NotRequired
from typing_extensions import Unpack
import js
from pyodide.ffi import create_proxy
from pyodide.http import pyfetch, FetchResponse

if TYPE_CHECKING:
    class FetchOptions(js._FetchOptions):
        json: NotRequired[Any]


async def fetch(url: str, **kwargs: Unpack[FetchOptions]) -> FetchResponse:
    if (data := kwargs.pop("json", None)) is not None:
        kwargs.setdefault("headers", {})["content-type"] = "application/json"
        kwargs["body"] = json.dumps(data)

    return await pyfetch(url, **kwargs)


async def get(url: str, /, **kwargs: Unpack[FetchOptions]) -> FetchResponse:
    kwargs["method"] = "GET"

    return await fetch(url, **kwargs)


async def post(url: str, /, **kwargs: Unpack[FetchOptions]) -> FetchResponse:
    kwargs["method"] = "POST"

    return await fetch(url, **kwargs)


async def patch(url: str, /, **kwargs: Unpack[FetchOptions]) -> FetchResponse:
    kwargs["method"] = "PATCH"

    return await fetch(url, **kwargs)


async def delete(url: str, /, **kwargs: Unpack[FetchOptions]) -> FetchResponse:
    kwargs["method"] = "DELETE"

    return await fetch(url, **kwargs)


class WebsocketState(Enum):
    CONNECTING = js.WebSocket.CONNECTING
    OPEN = js.WebSocket.OPEN
    CLOSING = js.WebSocket.CLOSING
    CLOSED = js.WebSocket.CLOSED


class Websocket:
    def __init__(self, url: str):
        self.inner = js.WebSocket.new(url)

        self.inner.addEventListener("close", create_proxy(self.on_close))
        self.inner.addEventListener("error", create_proxy(self.on_error))
        self.inner.addEventListener("open", create_proxy(self.on_open))
        self.inner.addEventListener("message", create_proxy(self.on_message))

        self.state = WebsocketState(self.inner.readyState)
        self.messages = asyncio.Queue[Any]()

        self.close_code: int | None = None
        self.close_reason: str | None = None
        self.closed: bool = False

    def on_close(self, event: js.CloseEvent):
        self.state = self.inner.readyState
        self.close_code = event.code
        self.close_reason = event.reason
        self.closed = True

    def on_message(self, event: js.MessageEvent):
        self.state = self.inner.readyState
        self.messages.put_nowait(event.data.to_py())

    def on_error(self, event: js.Event):
        self.state = self.inner.readyState

    def on_open(self, event: js.Event):
        self.state = self.inner.readyState

    def send(self, data: Any):
        self.inner.send(data)

    async def recv(self) -> Any:
        return await self.messages.get()

    async def close(self, *, code: int | None = None, reason: str | None = None):
        if code and reason:
            self.inner.close(code, reason)

        elif code:
            self.inner.close(code)

        elif reason:
            self.inner.close(0, reason)

    def __aiter__(self):
        return self

    def __anext__(self) -> Any:
        if self.state == WebsocketState.CLOSED:
            raise StopAsyncIteration("Websocket closed")

        return self.recv()
