from typing import Generic, TypeVar

T = TypeVar("T")


class JsProxy(Generic[T]):
    _: T


def create_proxy(f: T) -> JsProxy[T]:
    ...


def to_js(v: T) -> JsProxy[T]:
    ...
