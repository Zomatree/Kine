from __future__ import annotations

from typing import Any, Callable, TYPE_CHECKING
import weakref
import pyglet

if TYPE_CHECKING:
    from ..window import Window


class BaseWidgetMeta(type):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        obj = super().__call__(*args, **kwargs)
        obj.setup()
        return obj


class BaseWidget(metaclass=BaseWidgetMeta):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.calculate_size = True
        self.border_width = 0
        self.border_color = (0, 0, 0, 255)
        self.width = 0
        self.height = 0
        self.padding = 0
        self.margin = 0
        self.is_hover = False
        self.is_click = False
        self.is_select = False
        self.listeners: dict[str, list[Callable[..., Any]]] = {}
        self.parent: weakref.ProxyType[BaseWidget] | None = None
        self.window: Window | None = None

        self.color: tuple[int, int, int, int] = (0, 0, 0, 255)
        self.background_color: tuple[int, int, int, int] = (255, 255, 255, 255)

        self.batch = pyglet.graphics.Batch()
        self.background_group = pyglet.graphics.Group(order=0)
        self.foreground_group = pyglet.graphics.Group(order=1)

        self.children: list[BaseWidget] = []

    def __repr__(self):
        return f"<{self.__class__.__name__} x={self.x} y={self.y} w={self.width} h={self.height}>"

    def print_tree(self, level: int = 0):
        indent = "  " * level

        print(indent, self.__class__.__name__)

        for child in self.children:
            child.print_tree(level + 1)

    def setup(self):
        self.background = pyglet.shapes.BorderedRectangle(
            0,
            0,
            0,
            0,
            border=self.border_width,
            color=self.background_color,
            batch=self.batch,
            group=self.background_group,
        )

    def _set_window(self, window: Window):
        self.window = window

        for child in self.children:
            child._set_window(window)

    def add_child(self, widget: BaseWidget):
        widget.parent = weakref.proxy(self)
        widget.window = self.window
        self.children.append(widget)

    def remove_child(self, widget: BaseWidget):
        for i, child in enumerate(self.children):
            if child == widget:
                del self.children[i]

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.height, self.width)

    def add_listener(self, name: str, func: Callable[..., Any]):
        self.listeners.setdefault(name, []).append(func)

    def call_listeners(self, name: str, *args: Any):
        for func in self.listeners.get(name, []):
            func(*args)

    def is_intersecting(self, position: tuple[int, int]):
        return self.x <= position[0] <= (self.x + self.width) and self.y <= position[1] <= (self.y + self.height)

    @property
    def opacity(self) -> int:
        try:
            return self.color[3]  # type: ignore
        except IndexError:
            return 255

    @opacity.setter
    def opactity(self, value: int):
        self.color = (self.color[0], self.color[1], self.color[2], value)

    @property
    def background_opacity(self) -> int:
        try:
            return self.background_color[3]  # type: ignore
        except IndexError:
            return 255

    @background_opacity.setter
    def background_opacity(self, value: int):
        self.background_color = (self.background_color[0], self.background_color[1], self.background_color[2], value)

    def update(self, window: Window):
        self.background.x = self.x
        self.background.y = self.y

        self.background.opacity = self.background_color[3]

        self.background.border_color = self.border_color
        self.background._border = self.border_width
        self.background.color = self.background_color[0:3]
        width, height = self.calculate_bounding_box()

        if self.calculate_size:
            self.width = width
            self.height = height

        self.background.width = self.width
        self.background.height = self.height

    def draw(self, window: Window):
        self.update(window)
        # print("drawing", self.__class__.__name__, "at", self.x, self.y)
        self.batch.draw()

        for child in self.children:
            child.draw(window)

    def on_hover(self):
        self.is_hover = True

    def on_unhover(self):
        self.is_hover = False

    def on_click(self):
        self.is_click = True

    def on_unclick(self):
        self.is_click = False

    def on_select(self):
        self.is_select = True
        self.window.selected = self

    def on_unselect(self):
        self.is_select = False
        self.window.selected = None

    def on_text(self, text: str):
        pass

    def on_text_motion(self, motion: int):
        pass

    def after(self, *widgets: BaseWidget):
        parent = self.parent
        assert parent

        for i, widget in enumerate(widgets, parent.children.index(self) + 1):
            parent.children.insert(i, widget)

    def before(self, *widgets: BaseWidget):
        parent = self.parent
        assert parent

        idx = parent.children.index(self)
        parent.children[idx - 1].after(*widgets)

    def prepend(self, *widgets: BaseWidget):
        for widget in reversed(widgets):
            self.children.insert(0, widget)

    def remove(self):
        parent = self.parent
        assert parent

        idx = parent.children.index(self)
        del parent.children[idx]
        self.parent = None

    def replace_children(self, *widgets: BaseWidget):
        for widget in widgets:
            widget.parent = weakref.proxy(self)

        self.children = list(widgets)

    def replace_with(self, *widgets: BaseWidget):
        self.after(*widgets)
        self.remove()
