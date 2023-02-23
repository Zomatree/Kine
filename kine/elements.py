from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Generator, TypedDict, cast, TypeVar, Protocol

from typing_extensions import Self, Unpack

if TYPE_CHECKING:
    from .core import Node

__all__ = ("Element",)


class ElementArgs(TypedDict, total=False):
    pass


class Element:
    def __init__(self, **attributes: Unpack[ElementArgs]):
        self.children: tuple[Node, ...] = ()
        self.listeners: dict[str, Callable[[Any], None]] = {}
        self._key = None

        for name, value in list(attributes.items()):
            if name.startswith("on"):
                self.listeners[name[2:]] = cast(Callable[[Any], None], value)
                del attributes[name]

        self.attributes = attributes

    def __getitem__(self, children: Node | tuple[Node, ...] | Generator[Node, None, None]) -> Self:
        if isinstance(children, Generator):
            children = tuple(children)
        elif isinstance(children, tuple):
            pass
        else:
            children = (children,)

        self.children = children
        return self

    def key(self, key: str) -> Self:
        self._key = key
        return self


class GetAttrProto(Protocol):
    def __getitem__(self, children: Node | tuple[Node, ...] | Generator[Node, None, None]) -> Self:
        ...


T = TypeVar("T", bound=GetAttrProto)


class CGIMeta(type):
    def __getitem__(cls: type[T], children: Node | tuple[Node, ...] | Generator[Node, None, None]) -> T:
        return cls()[children]


class CGI(metaclass=CGIMeta):
    pass
