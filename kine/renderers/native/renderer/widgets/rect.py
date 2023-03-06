from __future__ import annotations

from .base import BaseWidget


class Rectangle(BaseWidget):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.calculate_size = False
        self.width = width
        self.height = height

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.width, self.height)
