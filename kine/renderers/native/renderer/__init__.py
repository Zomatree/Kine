from __future__ import annotations

from typing import Any, Callable, Literal
import weakref
import pyglet

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)


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
            0,
            0,
            0,
            0,
            border=self.border_width,
            color=self.background_color,
            batch=self.batch,
            group=self.background_group,
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
            pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)
            child.draw(window)
            pyglet.gl.glEnable(pyglet.gl.GL_DEPTH_TEST)

    def on_hover(self):
        self.is_hover = True

    def on_unhover(self):
        self.is_hover = False

    def on_click(self):
        self.is_click = True

    def on_unclick(self):
        self.is_click = False


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


class Label(BaseWidget):
    def __init__(self, text: str):
        super().__init__()
        self.background_color = (255, 255, 255, 0)
        self.text = text

    def setup(self):
        super().setup()
        self.label = pyglet.text.Label(self.text, batch=self.batch, group=self.background_group, color=self.color)

    def update(self, window: Window):
        super().update(window)

        self.label.text = self.text
        self.label.x = self.x + self.padding
        self.label.y = self.y + self.padding

        self.label.color = self.color
        self.background.color = self.parent.background_color  # opactity is just broken for some reason

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.label.content_width + self.padding * 2, self.label.content_height + self.padding * 2)


class Rectangle(BaseWidget):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.calculate_size = False
        self.width = width
        self.height = height

    def calculate_bounding_box(self) -> tuple[int, int]:
        return (self.width, self.height)


class Button(Flex):
    def __init__(self):
        super().__init__()
        self.border_width = 1
        self.padding = 2
        self.background_color = (0xF0, 0xF0, 0xF0, 255)
        self.hover_background_color = (255, 255, 255, 255)
        self._original_color = self.background_color
        self.border_color = (0x76, 0x76, 0x76, 0xFF)

    def on_hover(self):
        super().on_hover()
        self._original_color = self.background_color
        self.background_color = self.hover_background_color
        self.call_listeners("hover")

    def on_unhover(self):
        super().on_unhover()
        self.background_color = self._original_color
        self.call_listeners("unhover")

    def on_click(self):
        self.call_listeners("click")

    def on_unclick(self):
        self.call_listeners("unclick")


def recursive_find_at_pos(widgets: list[BaseWidget], position: tuple[int, int]) -> list[BaseWidget]:
    found: list[BaseWidget] = []

    for widget in widgets:
        if widget.is_intersecting(position):
            # print(f"intersecting {widget.__class__.__name__} at {position}")
            found.append(widget)
            found.extend(recursive_find_at_pos(widget.children, position))

    return found


class Root(Row):
    def __init__(self):
        super().__init__()
        self.calculate_size = False

    def update(self, window: Window):
        self.width = window.width
        self.height = window.height

        super().update(window)


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.root = Root()
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

    def run(self):
        event_loop = pyglet.app.EventLoop()
        event_loop.run()


def main():
    window = Window()
    window.root.padding = 5

    for i in range(10):
        button = Button()
        button.add_child(Label(str(i)))

        window.add_child(button)

    window.run()
