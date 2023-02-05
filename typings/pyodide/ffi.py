from typing import Generic, TypeVar

T = TypeVar("T")


class Proxy(Generic[T]):
    _: T


def create_proxy(f: T) -> Proxy[T]:
    ...
