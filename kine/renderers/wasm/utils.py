from __future__ import annotations

import asyncio
from enum import Enum
from typing import Any
from typing_extensions import Unpack
import js
from pyodide.ffi import create_proxy


class Response:
    def __init__(self, inner: js.Response):
        self.inner = inner

    async def text(self) -> str:
        return await self.inner.text()

    async def json(self) -> Any:
        data = await self.inner.json()
        return data.to_py()


async def fetch(url: str, **kwargs: Unpack[js._FetchOptions]) -> Response:
    return Response(await js.fetch(url, kwargs))


async def get(url: str, /, **kwargs: Unpack[js._FetchOptions]) -> Response:
    kwargs["method"] = "GET"

    return await fetch(url, **kwargs)


async def post(url: str, /, **kwargs: Unpack[js._FetchOptions]) -> Response:
    kwargs["method"] = "POST"

    return await fetch(url, **kwargs)


async def patch(url: str, /, **kwargs: Unpack[js._FetchOptions]) -> Response:
    kwargs["method"] = "PATCH"

    return await fetch(url, **kwargs)


async def delete(url: str, /, **kwargs: Unpack[js._FetchOptions]) -> Response:
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

    def on_message(self, event: js.MessageEvent[Any]):
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
