from __future__ import annotations

from typing import Any

import glfw
import skia
import stretchable
from OpenGL import GL
from stretchable import Style as Layout
from stretchable.style import PT
import stretchable.node

from .events import MouseEvent
from .node import Node, RootNode
from .utils import WHITE, CursorType
from .window_utils import glfw_window, skia_surface


def draw_node(canvas: Any, node: RootNode):
    node.draw(canvas)

    for child in node:
        assert isinstance(child, RootNode)
        draw_node(canvas, child)


class Window:
    def __init__(self, title: str, width: int, height: int):
        self.title = title
        self.width: int = width
        self.height: int = height
        self.cursor_position: tuple[int, int] = (0, 0)
        self.current_nodes = self.nodes()

    def nodes(self) -> RootNode:
        return Node(layout=Layout(size=(self.width * PT, self.height * PT)))

    def on_resize(self, window: glfw.Window, width: int, height: int):
        self.width = width
        self.height = height

        self.redraw(window)

    def on_click(self, window: glfw.Window, button: int, action: int, mods: int):
        if button == 0 and action == 1:  # left click, button down
            event = MouseEvent(button, self.cursor_position)
            self.current_nodes.execute_events("click", lambda n: box_contains_pos(n.get_box(relative=False), *self.cursor_position), event)

    def update_state_from_external(self, window: Any):
        cur_pos = glfw.get_cursor_pos(window)
        self.cursor_position = (int(cur_pos[0]), int(cur_pos[1]))

    def update_node_to_current_state(self, node: RootNode):
        box = node.get_box(relative=False)

        in_box = box_contains_pos(box, *self.cursor_position)

        if in_box and node.state.hover is False:
            node.state.hover = True
        elif not in_box:
            node.state.hover = False

        for child in node:
            assert isinstance(child, RootNode)
            self.update_node_to_current_state(child)

    def set_cursor_type(self, window: Any):
        hovered_nodes = self.current_nodes.find_where(lambda node: box_contains_pos(node.get_box(relative=False), *self.cursor_position))

        for node in reversed(hovered_nodes):
            if cursor := node.node_style.cursor:
                match cursor:
                    case CursorType.DEFAULT:
                        glfw_cur = glfw.ARROW_CURSOR
                    case CursorType.POINTER:
                        glfw_cur = glfw.HAND_CURSOR

                glfw.set_cursor(window, glfw._GLFWcursor(glfw_cur))

                break

    def redraw(self, window: glfw.Window):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        node = self.nodes()
        self.current_nodes = node

        node.mark_dirty()
        node.compute_layout((self.width, self.height), use_rounding=True)

        self.update_state_from_external(window)
        self.update_node_to_current_state(node)
        self.set_cursor_type(window)

        with skia_surface(window) as surface:
            with surface as canvas:
                canvas.drawRect(skia.Rect(0, 0, self.width, self.height), skia.Paint(Color=WHITE.inner))

                draw_node(canvas, node)

            surface.flushAndSubmit()
            glfw.swap_buffers(window)

    def run(self):
        with glfw_window(self.width, self.height, self.title) as window:
            glfw.set_window_size_callback(window, self.on_resize)
            glfw.set_mouse_button_callback(window, self.on_click)

            while not glfw.window_should_close(window):
                self.redraw(window)
                glfw.wait_events()

def box_contains_pos(box: stretchable.Box, x: int, y: int) -> bool:
    return (box.x < x < (box.x + box.width)) and (box.y < y < (box.y + box.height))
