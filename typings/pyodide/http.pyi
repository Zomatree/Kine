from io import StringIO
from typing import Any, Literal, TypedDict, Unpack
from js import AbortSignal

class _FetchOptions(TypedDict, total=False):
    method: str
    headers: dict[str, str]
    body: Any
    mode: str
    credentials: Literal["omit", "same-origin", "include"]
    cache: Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]
    redirect: Literal["follow", "error", "manual"]
    referrer: str
    referrerPolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]

    integrity: str
    keepalive: bool
    signal: AbortSignal

class FetchResponse:
    def __init__(self, url: str, js_response: Any) -> None: ...
    async def bytes(self) -> bytes: ...
    def clone(self) -> FetchResponse: ...
    async def json(self, **kwargs: Any) -> Any: ...
    async def memoryview(self) -> memoryview: ...
    def string(self) -> str: ...
    def unpack_archive(
        self, *, extract_dir: str | None = None, format: Literal["zip", "tar", "gztar", "bztar"] | None = None
    ) -> None: ...

    body_used: bool
    ok: bool
    redirect: bool
    status: int
    status_text: str
    type: str

def open_url(url: str) -> StringIO: ...
async def pyfetch(url: str, **kwargs: Unpack[_FetchOptions]) -> FetchResponse: ...
