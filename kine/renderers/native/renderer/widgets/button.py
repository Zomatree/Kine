from __future__ import annotations
import pyglet

from .flex import Flex


class Button(Flex):
    def __init__(self):
        super().__init__()
        self.border_width = 1
        self.padding = 5
        self.regular_background_color = (0xF0, 0xF0, 0xF0, 255)
        self.hover_background_color = (255, 255, 255, 255)
        self.border_color = (0x76, 0x76, 0x76, 0xFF)

    def setup(self):
        self.background_color = self.regular_background_color
        super().setup()

    def on_hover(self):
        super().on_hover()
        self.background_color = self.hover_background_color
        self.window.set_cursor("hand")
        self.call_listeners("hover")

    def on_unhover(self):
        super().on_unhover()
        self.background_color = self.regular_background_color
        self.window.set_cursor(None)
        self.call_listeners("unhover")

    def on_click(self):
        self.call_listeners("click")

    def on_unclick(self):
        self.call_listeners("unclick")
