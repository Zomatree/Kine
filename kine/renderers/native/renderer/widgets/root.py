from __future__ import annotations

from typing import TYPE_CHECKING
from .flex import Row

if TYPE_CHECKING:
    from ..window import Window


class Root(Row):
    def __init__(self, window: Window):
        super().__init__()
        self.window = window
        self.calculate_size = False

    def update(self, window: Window):
        self.width = window.width
        self.height = window.height

        super().update(window)
