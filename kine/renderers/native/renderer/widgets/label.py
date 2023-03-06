from __future__ import annotations

from typing import TYPE_CHECKING
import pyglet

from .base import BaseWidget

if TYPE_CHECKING:
    from ..window import Window


class Label(BaseWidget):
    def __init__(self, text: str, font_size: int | None = None):
        super().__init__()
        self.background_color = (255, 255, 255, 0)
        self.text = text
        self.font_size = font_size

    def setup(self):
        super().setup()
        self.label = pyglet.text.Label(
            self.text,
            font_name="Comic Sans MS Regular",
            batch=self.batch,
            group=self.background_group,
            color=self.color,
            font_size=self.font_size,
        )

    def update(self, window: Window):
        super().update(window)

        self.label.text = self.text
        self.label.x = self.x + self.padding
        self.label.y = self.y + self.padding
        self.label.font_size = self.font_size

        self.label.color = self.color
        # self.background.color = self.parent.background_color  # opactity is just broken for some reason

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.label.content_width + self.padding * 2, (self.label.font_size or 12) + (self.padding * 2))
