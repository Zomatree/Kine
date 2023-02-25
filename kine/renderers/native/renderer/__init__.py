from __future__ import annotations

from typing import Any, Callable
import weakref
import pyglet


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
        self.width = 0
        self.height = 0
        self.padding = 0
        self.margin = 0
        self.is_hover = False
        self.is_click = False
        self.listeners: dict[str, list[Callable[..., Any]]] = {}
        self.parent: weakref.ProxyType[BaseWidget] | None = None

        self.color: tuple[int, int, int, int] = (0, 0, 0, 255)
        self.background_color: tuple[int, int, int, int] = (255, 255, 255, 255)

        self.batch = pyglet.graphics.Batch()
        self.background_group = pyglet.graphics.Group(order=0)
        self.foreground_group = pyglet.graphics.Group(order=1)

        self.children: list[BaseWidget] = []

    def setup(self):
        self.background = pyglet.shapes.BorderedRectangle(
            0, 0, 0, 0, border=0, color=self.background_color, batch=self.batch, group=self.background_group
        )

    def add_child(self, widget: BaseWidget):
        widget.parent = weakref.proxy(self)
        self.children.append(widget)

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.height, self.width)

    def add_listener(self, name: str, func: Callable[..., Any]):
        self.listeners.setdefault(name, []).append(func)

    def call_listeners(self, name: str, *args: Any):
        for func in self.listeners.get(name, []):
            func(*args)

    def is_intersecting(self, position: tuple[int, int]):
        return self.x <= position[0] <= (self.x + self.width) and self.y <= position[1] <= (self.y + self.height)

    def update(self, window: Window):
        self.background.x = self.x
        self.background.y = self.y

        self.background.opacity = self.background_color[3]
        self.background.color = self.background_color

        width, height = self.calculate_bounding_box()

        if self.calculate_size:
            self.width = width
            self.height = height

        self.background.width = self.width + (self.padding * 2)
        self.background.height = self.height + (self.padding * 2)

    def draw(self, window: Window):
        # print("drawing", self.__class__.__name__, "at", self.x, self.y)
        self.update(window)
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


class Row(BaseWidget):
    def calculate_bounding_box(self) -> tuple[int, int]:
        width = 0
        height = 0

        for child in self.children:
            child.x = self.x + width + self.padding + child.margin
            child.y = self.y + self.padding + child.margin
            width += self.padding + child.margin

            child_width, child_height = child.calculate_bounding_box()
            margin_height = child_height + (child.margin * 2)

            if margin_height > height:
                height = margin_height

            width += child_width + self.padding + child.margin

        return (width - self.padding, height)


class Column(BaseWidget):
    def calculate_bounding_box(self) -> tuple[int, int]:
        width = 0
        height = 0

        for child in self.children:
            child.x = self.x + self.padding + child.margin
            child.y = self.y + height + self.padding + child.margin
            height += self.padding + child.margin

            child_width, child_height = child.calculate_bounding_box()
            margin_width = child_width + (child.margin * 2)

            if margin_width > width:
                width = margin_width

            height += child_height + self.padding + child.margin

        return (width, height - self.padding)


class Label(BaseWidget):
    def __init__(self, text: str):
        super().__init__()
        self.background_color = (0, 0, 0, 0)
        self.text = text

    def setup(self):
        super().setup()
        self.label = pyglet.text.Label(self.text, batch=self.batch, group=self.background_group, color=self.color)

    def update(self, window: Window):
        super().update(window)

        self.label.text = self.text
        self.label.x = self.x
        self.label.y = self.y
        self.label.color = self.color

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.label.content_width, self.label.content_height)


class Block(BaseWidget):
    pass


class Rectangle(BaseWidget):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.width, self.height)


class Button(BaseWidget):
    def __init__(self):
        super().__init__()
        self.padding = 5
        self.background_color = (200, 200, 200, 255)

    def on_hover(self):
        super().on_hover()
        self.background.color = (255, 255, 255, 255)
        self.call_listeners("hover")

    def on_unhover(self):
        super().on_unhover()
        self.background.color = self.background_color
        self.call_listeners("unhover")

    def on_click(self):
        self.call_listeners("click")

    def on_unclick(self):
        self.call_listeners("unclick")


def recursive_find_at_pos(widgets: list[BaseWidget], position: tuple[int, int]) -> list[BaseWidget]:
    found: list[BaseWidget] = []

    for widget in widgets:
        if widget.is_intersecting(position):
            found.append(widget)
            found.extend(recursive_find_at_pos(widget.children, position))

    return found


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.root = Row()
        self.root.calculate_size = False
        self.root.width = self.width
        self.root.height = self.height
        self.after: dict[str, dict[int, Callable[[Any], bool]]] = {}

    def add_child(self, widget: BaseWidget):
        widget.parent = weakref.proxy(self.root)
        self.root.children.append(widget)

    def add_after(self, name: str, f: Callable[[Any], bool]):
        cbs = self.after.setdefault(name, {})

        cbs[len(cbs)] = f

    def run_after(self, name: str, pos: tuple[int, int]):
        for k, v in list(self.after.get(name, {}).items()):
            if v(pos):
                del self.after[name][k]

    def recursive_run_at_position(self, pos: tuple[int, int], data: Any, f: Callable[[BaseWidget, Any], bool]):
        widgets = recursive_find_at_pos(self.root.children, pos)

        for widget in reversed(widgets):
            should_stop = f(widget, data)

            if should_stop:
                break

    def hover_callback(self, widget: BaseWidget, data: Any):
        if not widget.is_hover:
            widget.on_hover()

            def after(pos: tuple[int, int]) -> bool:
                if not widget.is_intersecting(pos):
                    widget.on_unhover()
                    return True

                return False

            self.add_after("mouse", after)

        return False

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.run_after("mouse", (x, y))
        self.recursive_run_at_position((x, y), None, self.hover_callback)

    def click_callback(self, widget: BaseWidget, data: Any):
        if data["button"] & pyglet.window.mouse.LEFT and not widget.is_click:
            widget.on_click()

            def after(pos: tuple[int, int]) -> bool:
                if not widget.is_intersecting(pos):
                    widget.on_unclick()
                    return True

                return False

            self.add_after("mouse_press", after)

        return False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: Any):
        self.run_after("mouse", (x, y))
        self.recursive_run_at_position((x, y), {"button": button}, self.click_callback)

    def on_draw(self):  # type: ignore - type definition is invalid
        self.clear()
        self.root.draw(self)


def main():
    window = Window()

    row = Row()
    row.margin = 10
    row.padding = 5
    row.background_color = (255, 0, 0, 255)

    rect = Rectangle(30, 10)
    rect.background_color = (0, 255, 0, 255)
    row.add_child(rect)

    text = Label("Hello World")
    text.background_color = (0, 255, 0, 255)
    text.color = (0, 0, 255, 100)
    row.add_child(text)

    rect = Rectangle(30, 20)
    rect.background_color = (0, 255, 0, 255)
    row.add_child(rect)

    column = Column()
    column.background_color = (0, 255, 0, 255)

    rect = Rectangle(10, 20)
    rect.margin = 5
    column.add_child(rect)

    rect = Rectangle(10, 20)
    rect.margin = 10
    column.add_child(rect)

    row.add_child(column)

    rect = Rectangle(50, 1)
    rect.background_color = (0, 255, 0, 255)
    row.add_child(rect)

    window.add_child(row)

    event_loop = pyglet.app.EventLoop()
    event_loop.run()
