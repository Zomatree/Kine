from __future__ import annotations

from typing import TYPE_CHECKING
import pyglet
import pyglet.window.key as Key

from .label import Label

if TYPE_CHECKING:
    from ..window import Window


class Input(Label):
    def __init__(self, text: str = ""):
        super().__init__(text=text)
        self._text = list(text)
        self.padding = 6
        self.cursor_position = 0
        self.border_color = (0, 0, 0, 255)
        self.border_width = 1
        self.background_color = (255, 255, 255, 255)
        self.cursor_positions: list[int] = [0]

    def setup(self):
        super().setup()
        self.cursor = pyglet.shapes.Rectangle(0, 0, 1, 0, color=(0, 0, 0, 255))
        self.cursor.visible = False

    def update(self, window: Window):
        super().update(window)
        self.cursor.x = self.label.x + self.cursor_positions[self.cursor_position]
        self.cursor.y = self.y + self.padding - 1
        self.cursor.height = (self.label.font_size or 12) + 2

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (40 + self.padding * 2, (self.label.font_size or 12) + (self.padding * 2))

    def draw(self, window: Window):
        super().draw(window)
        self.cursor.draw()

    def set_cursor_position(self, position: int):
        self.cursor_position += position

    def _insert_char(self, index: int, char: str):
        if index == len(self._text):
            self._text.append(char)
            self.label.text = self.text
            self.cursor_positions.append(self.label.content_width)
        else:
            self._text.insert(index, char)

            original_length = self.label.content_width
            orginal_position = self.cursor_positions[index]

            self.label.text = self.text
            new_length = self.label.content_width
            width = new_length - original_length

            self.cursor_positions.insert(index + 1, orginal_position + width)
            self.cursor_positions[index + 2 :] = [pos + width for pos in self.cursor_positions[index + 2 :]]

    def _remove_char(self, index: int):
        if index == len(self._text):
            self._text.pop()
            self.cursor_positions.pop()
        else:
            del self._text[index]
            position = self.cursor_positions.pop(index)
            after = self.cursor_positions[index]
            width = after - position
            self.cursor_positions[index:] = [pos - width for pos in self.cursor_positions[index:]]

    @property
    def text(self) -> str:
        return "".join(self._text)

    @text.setter
    def text(self, text: str):
        self._text = list(text)

    def on_select(self):
        super().on_select()

        self.background_color = (255, 0, 0, 255)
        self.cursor_position = len(self._text)
        self.cursor.visible = True

    def on_unselect(self):
        super().on_unselect()

        self.background_color = (255, 255, 255, 255)
        self.cursor.visible = False

    def on_key(self, char: int):
        ...

    def on_text(self, text: str):
        self._insert_char(self.cursor_position, text[0])
        self.cursor_position += 1

    def on_text_motion(self, motion: int):
        match motion:
            case Key.MOTION_UP:
                ...
            case Key.MOTION_DOWN:
                ...
            case Key.MOTION_LEFT:
                self.cursor_position = max(self.cursor_position - 1, 0)
            case Key.MOTION_RIGHT:
                self.cursor_position = min(self.cursor_position + 1, len(self.text))
            case Key.MOTION_PREVIOUS_WORD:
                ...
            case Key.MOTION_NEXT_WORD:
                ...
            case Key.MOTION_BEGINNING_OF_LINE:
                ...
            case Key.MOTION_END_OF_LINE:
                ...
            case Key.MOTION_PREVIOUS_PAGE:
                ...
            case Key.MOTION_NEXT_PAGE:
                ...
            case Key.MOTION_BEGINNING_OF_FILE:
                self.cursor_position = 0
            case Key.MOTION_END_OF_FILE:
                ...
            case Key.MOTION_BACKSPACE:
                if self._text:
                    self._remove_char(self.cursor_position - 1)
                    self.cursor_position = max(0, self.cursor_position - 1)

            case Key.MOTION_DELETE:
                if len(self._text) != self.cursor_position:
                    self._remove_char(self.cursor_position)
            case _:
                pass
