from __future__ import annotations

import skia
from stretchable import Node as BaseNode
import stretchable
from stretchable.style import PT, Style as Layout
from typing import Any, Callable

from stretchable.style.geometry.size import SizePoints

from .utils import Style, NodeState, Color, CLEAR, BLACK
from .events import BaseEvent

class RootNode(BaseNode):
    def __init__(
            self,
            id: str | None = None,
            *,
            layout: Layout | None = None,
            style: Style | None = None,
            hover_style: Style | None = None,
            events: dict[str, list[Callable[[Any], Any]]] | None = None
        ):
        super().__init__(key=id, style=layout)

        self.node_style = style or Style()
        self.hover_style = hover_style or Style()
        self.state = NodeState()
        self.events: dict[str, list[Callable[[BaseEvent], Any]]] = events or {}

    def add_event_listener(self, name: str, listener: Callable[[BaseEvent], Any]) -> None:
        self.events.setdefault(name, []).append(listener)

    def get_listeners_for_event(self, name: str, requirement: Callable[[RootNode], bool]) -> list[list[Callable[[BaseEvent], Any]]]:
        if not requirement(self):
            return []

        listeners = [self.events.get(name, [])]

        for child in self:
            assert isinstance(child, RootNode)

            if requirement(child):
                listeners.extend(child.get_listeners_for_event(name, requirement))

        return listeners

    def execute_events(self, name: str, requirement: Callable[[RootNode], bool], event: BaseEvent):
        listeners = self.get_listeners_for_event(name, requirement)

        for node_listeners in reversed(listeners):
            for node_listener in node_listeners:
                node_listener(event)

            if not event.bubbles:
                break

    def get_background_style(self) -> Color | None:
        return (self.hover_style.background or self.node_style.background) if self.state.hover else self.node_style.background

    def get_foreground_style(self) -> Color | None:
        color = (self.hover_style.foreground or self.node_style.foreground) if self.state.hover else self.node_style.foreground

        if not color and self.parent:
            assert isinstance(self.parent, RootNode)

            return self.parent.get_foreground_style()

        return color

    def get_font_size(self) -> int | None:
        font_size = (self.hover_style.font_size or self.node_style.font_size) if self.state.hover else self.node_style.font_size

        if not font_size and self.parent:
            assert isinstance(self.parent, RootNode)

            return self.parent.get_font_size()

        return font_size

    def find_where(self, cb: Callable[[RootNode], bool]) -> list[RootNode]:
        nodes: list[RootNode] = []

        if cb(self):
            nodes.append(self)

        for child in self:
            assert isinstance(child, RootNode)
            nodes.extend(child.find_where(cb))

        return nodes

    def draw_bg(self, box: stretchable.Box, canvas: Any):
        canvas.drawRect(skia.Rect(box.x, box.y, box.x + box.width, box.y + box.height), skia.Paint(Color=(self.get_background_style() or CLEAR).inner))

    def draw(self, canvas: Any) -> stretchable.Box:
        raise NotImplementedError

class Node(RootNode):
    def draw(self, canvas: Any) -> stretchable.Box:
        box = self.get_box(relative=False)
        self.draw_bg(box, canvas)

        return box

class TextNode(Node):
    def __init__(
            self,
            text: str,
            id: str | None = None,
            layout: stretchable.Style | None = None,
            style: Style | None = None,
            hover_style: Style | None = None
        ):
        super().__init__(id=id, layout=layout, style=style, hover_style=hover_style)

        self.font = skia.Font()

        self.text = text
        self.measure = self.text_measure

    def text_measure(self, *_: Any):
        if font_size := self.get_font_size():
            self.font.setSize(font_size)

        height = self.font.getSize()
        width = self.font.measureText(self.text)

        return SizePoints(width * PT, height * PT)

    def draw(self, canvas: Any) -> stretchable.Box:
        box = self.get_box(relative=False)
        self.draw_bg(box, canvas)

        canvas.drawSimpleText(self.text, box.x, box.y + box.height, self.font, skia.Paint(Color=(self.get_foreground_style() or BLACK).inner))

        return box