from __future__ import annotations

from dataclasses import dataclass
from stretchable.style.geometry import LengthPointsPercent
from enum import Enum, auto
from typing import Any, Generic, TypeVar, get_args

from attr import define, field
import skia

T = TypeVar("T")

class Color:
    def __init__(self, inner: Any):
        self.inner = inner

    @classmethod
    def rgb(cls, hex: int) -> Any:
        return cls(skia.Color(hex >> 16, hex >> 8 & 0xFF, hex & 0xFF))

RED: Color = Color(skia.Color(0xFF, 0x0, 0x0, 0xFF))
GREEN: Color = Color(skia.Color(0x0, 0xFF, 0x0, 0xFF))
BLUE: Color = Color(skia.Color(0x0, 0x0, 0xFF, 0xFF))
YELLOW: Color = Color(skia.Color(0xFF, 0xFF, 0x0, 0xFF))
CYAN: Color = Color(skia.Color(0x0, 0xFF, 0xFF, 0xFF))
MAGENTA: Color = Color(skia.Color(0xFF, 0x0, 0xFF, 0xFF))
BLACK: Color = Color(skia.Color(0x0, 0x0, 0x00, 0xFF))
WHITE: Color = Color(skia.Color(0xFF, 0xFF, 0xFF, 0xFF))
CLEAR: Color = Color(skia.Color(0x0, 0x0, 0x0, 0x00))


@dataclass
class NodeState:
    hover: bool = False

class CursorType(Enum):
    DEFAULT = auto()
    POINTER = auto()

class Corners(Generic[T]):
    _type_T: T
    __orig_bases__: tuple[Any, ...]

    def __init_subclass__(cls) -> None:
        cls._type_T = get_args(cls.__orig_bases__[0])[0]

    def __init__(self, topleft: T, topright: T, bottomright: T, bottomleft: T):
        self.topleft: T = self._type_T.from_any(topleft)  # type: ignore
        self.topright: T = self._type_T.from_any(topright)  # type: ignore
        self.bottomright: T = self._type_T.from_any(bottomright)  # type: ignore
        self.bottomleft: T = self._type_T.from_any(bottomleft)  # type: ignore

    @classmethod
    def from_any(cls, value: Any):
        if isinstance(value, cls):
            return value
        elif isinstance(value, (tuple, list)):
            length = len(value)

            if length == 1:
                return cls(value[0], value[0], value[0], value[0])
            if length == 2:
                return cls(value[0], value[0], value[1], value[1])
            elif length == 3:
                return cls(value[0], value[1], value[1], value[2])
            else:
                return cls(*value)
        else:
            return cls(value, value, value, value)

class BorderRadius(Corners[LengthPointsPercent]):
    pass

@define(kw_only=True)
class Style:
    background: Color | None = None
    foreground: Color | None = None
    cursor: CursorType | None = None
    font_size: int | None = None
    border_color: Color | None = None
    border_radius: BorderRadius = field(default=0.0, converter=BorderRadius.from_any)
