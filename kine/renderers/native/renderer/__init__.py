from __future__ import annotations

from typing import Any, Callable, Iterable, Literal
import weakref
import pyglet
import pyglet.window.key as Key

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
        self.regular_background_color = (0xF0, 0xF0, 0xF0, 255)
        self.hover_background_color = (255, 255, 255, 255)
        self.border_color = (0x76, 0x76, 0x76, 0xFF)

    def setup(self):
        self.background_color = self.regular_background_color
        super().setup()

    def on_hover(self):
        super().on_hover()
        self.background_color = self.hover_background_color
        self.call_listeners("hover")

    def on_unhover(self):
        super().on_unhover()
        self.background_color = self.regular_background_color
        self.call_listeners("unhover")

    def on_click(self):
        self.call_listeners("click")

    def on_unclick(self):
        self.call_listeners("unclick")


class Input(Label):
    def __init__(self, text: str = ""):
        super().__init__(text=text)
        self._text = list(text)
        self.padding = 5
        self.cursor_position = 0
        self.border_color = (0, 0, 0, 255)
        self.border_width = 1
        self.background_color = (255, 255, 255, 255)
        self.cursor_positions: list[int] = [0]

    def setup(self):
        super().setup()
        self.label.height = self.label.font_size
        self.width = min(self.width, 40)
        self.cursor = pyglet.shapes.Rectangle(0, 0, 1, self.label.font_size or 12, color=(0, 255, 0, 255))
        self.cursor.visible = False

    def update(self, window: Window):
        super().update(window)
        self.cursor.x = self.label.x + self.cursor_positions[self.cursor_position]
        self.cursor.y = self.y + self.padding - 1
        self.cursor.height = (self.label.font_size or 12) + 2

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


def recursive_find_at_pos(widgets: Iterable[BaseWidget], position: tuple[int, int]) -> list[BaseWidget]:
    found: list[BaseWidget] = []

    for widget in widgets:
        if widget.is_intersecting(position):
            found.append(widget)
            found.extend(recursive_find_at_pos(widget.children, position))

    return found


class Root(Row):
    def __init__(self, window: Window):
        super().__init__()
        self.window = window
        self.calculate_size = False

    def update(self, window: Window):
        self.width = window.width
        self.height = window.height

        super().update(window)


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.root = Root(self)
        self.root.calculate_size = False
        self.root.width = self.width
        self.root.height = self.height
        self.after: dict[str, dict[int, Callable[[tuple[int, int], Any], bool]]] = {}
        self.selected: BaseWidget | None = None

    def add_child(self, widget: BaseWidget):
        self.root.add_child(widget)

    def add_after(self, name: str, f: Callable[[tuple[int, int], Any], bool]):
        cbs = self.after.setdefault(name, {})

        cbs[len(cbs)] = f

    def run_after(self, name: str, pos: tuple[int, int], data: Any = None):
        for k, v in list(self.after.get(name, {}).items()):
            if v(pos, data):
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

            def after(pos: tuple[int, int], _: Any) -> bool:
                if widget.is_hover and not widget.is_intersecting(pos):
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

        return False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: Any):
        self.run_after("mouse", (x, y), {"button": button})
        self.recursive_run_at_position((x, y), {"button": button, "pos": (x, y)}, self.click_callback)

    def on_draw(self):  # type: ignore - type definition is invalid
        self.clear()
        self.root.draw(self)

    def on_text(self, text: str):
        if widget := self.selected:
            widget.on_text(text)

    def on_text_motion(self, motion: int):
        if widget := self.selected:
            widget.on_text_motion(motion)

    def run(self):
        event_loop = pyglet.app.EventLoop()
        event_loop.run()


def main():
    window = Window()
    window.root.padding = 5

    window.add_child(Input())

    window.root.print_tree()
    window.run()
