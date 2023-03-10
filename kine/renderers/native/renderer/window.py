from __future__ import annotations

from typing import Any, Callable
import pyglet

from .widgets import Root, BaseWidget
from .utils import recursive_find_at_pos


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.root = Root(self)
        self.root.calculate_size = False
        self.root.width = self.width
        self.root.height = self.height
        self.after: dict[str, dict[int, Callable[[tuple[int, int], Any], bool]]] = {}
        self.selected: BaseWidget | None = None

    def set_cursor(self, cursor: str | None):
        cursor = self.get_system_mouse_cursor(cursor)
        self.set_mouse_cursor(cursor)

    def add_child(self, widget: BaseWidget):
        self.root.add_child(widget)
        widget._set_window(self)

    def add_after(self, name: str, f: Callable[[tuple[int, int], Any], bool]):
        cbs = self.after.setdefault(name, {})

        cbs[len(cbs)] = f

    def run_after(self, name: str, pos: tuple[int, int], data: Any = None):
        for k, v in list(self.after.get(name, {}).items()):
            if v(pos, data):
                del self.after[name][k]

    def recursive_run_at_position(self, pos: tuple[int, int], data: Any, f: Callable[[BaseWidget, Any], bool]):
        widgets = recursive_find_at_pos(self.root.children, pos)
        print(widgets)

        for widget in reversed(widgets):
            should_stop = f(widget, data)

            if should_stop:
                break

    def hover_callback(self, widget: BaseWidget, data: Any):
        if not widget.is_hover:
            widget.on_hover()

            def after(pos: tuple[int, int], _: Any) -> bool:
                if widget.is_hover and not widget.is_intersecting(pos):
                    print("unhover")
                    widget.on_unhover()

                    return True

                return False

            self.add_after("mouse", after)

        return False

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.run_after("mouse", (x, y), {"button": 0})
        self.recursive_run_at_position((x, y), None, self.hover_callback)

    def click_callback(self, widget: BaseWidget, data: Any):
        if data["button"] & pyglet.window.mouse.LEFT:
            if not widget.is_click:
                widget.on_click()

                def click_after(pos: tuple[int, int], data: Any) -> bool:
                    if not (data["button"] & pyglet.window.mouse.LEFT) or not widget.is_intersecting(pos):
                        widget.on_unclick()
                        return True

                    return False

                self.add_after("mouse", click_after)

            if not widget.is_select:
                widget.on_select()

                def select_after(pos: tuple[int, int], data: Any) -> bool:
                    if data["button"] & pyglet.window.mouse.LEFT and not widget.is_intersecting(pos):
                        widget.on_unselect()
                        return True

                    return False

                self.add_after("mouse", select_after)
                return True

        return False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: Any):
        self.run_after("mouse", (x, y), {"button": button})
        self.recursive_run_at_position((x, y), {"button": button, "pos": (x, y)}, self.click_callback)

    def on_draw(self):  # type: ignore - type definition is invalid
        self.clear()
        self.root.draw(self)

    def on_text(self, text: str):
        print(text, self.selected)
        if widget := self.selected:
            widget.on_text(text)

    def on_text_motion(self, motion: int):
        if widget := self.selected:
            widget.on_text_motion(motion)

    def run(self):
        event_loop = pyglet.app.EventLoop()
        event_loop.run()
