from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from .base import BaseWidget


class Flex(BaseWidget):
    def __init__(self, direction: Literal["row", "column"] = "row"):
        super().__init__()
        self.direction = direction

    def calculate_bounding_box(self) -> tuple[int, int]:
        gap = self.padding + self.border_width
        width = gap
        height = gap

        if self.direction == "row":
            for child in self.children:
                width += child.margin

                child.x = self.x + width
                child.y = self.y + child.margin + gap

                child_width, child_height = child.calculate_bounding_box()
                margin_height = child_height + (child.margin * 2) + gap

                if margin_height > height:
                    height = margin_height

                width += child_width + child.margin
        else:
            for child in self.children:
                height += child.margin

                child.x = self.x + child.margin + gap
                child.y = self.y + height

                child_width, child_height = child.calculate_bounding_box()
                margin_width = child_width + (child.margin * 2) + gap

                if margin_width > width:
                    width = margin_width

                height += child_height + child.margin

        width += gap
        height += gap

        return (width, height)


class Row(Flex):
    def __init__(self):
        super().__init__("row")


class Column(Flex):
    def __init__(self):
        super().__init__("column")
