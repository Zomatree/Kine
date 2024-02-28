from __future__ import annotations

import skia
from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

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

@dataclass(kw_only=True)
class Style:
    background: Color | None = None
    foreground: Color | None = None
    cursor: CursorType | None = None
    font_size: int | None = None
