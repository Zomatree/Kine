from __future__ import annotations

from typing import Any, Callable

import attrs
import skia
import stretchable
from stretchable import Edge, Node as BaseNode
from stretchable.style import PT, NAN
from stretchable.style import Style as Layout, FlexDirection
from stretchable.style.geometry.size import SizePoints, SizeAvailableSpace
from stretchable.style.geometry.rect import RectPointsPercent

from .events import BaseEvent
from .utils import BLACK, CLEAR, WHITE, Color, NodeState, Style


class RootNode(BaseNode):
    def __init__(
            self,
            id: Any | None = None,
            *,
            layout: Layout | None = None,
            style: Style | None = None,
            hover_style: Style | None = None,
            events: dict[str, list[Callable[[Any], Any]]] | None = None
        ):
        super().__init__(style=layout)

        self.id = id
        self.node_style = style or Style()
        self.hover_style = hover_style or Style()
        self.state = NodeState()
        self.events: dict[str, list[Callable[[BaseEvent], Any]]] = events or {}

    def replace_with(self, *nodes: RootNode):
        if parent := self.parent:
            position = parent.index(self)
            
            parent.pop(position)
            
            for node in nodes[::-1]:
                parent.insert(position, node)

    def after(self, *nodes: RootNode):
        if parent := self.parent:
            position = parent.index(self)
            
            for node in nodes[::-1]:
                parent.insert(position + 1, node)

    def before(self, *nodes: RootNode):
        if parent := self.parent:
            position = parent.index(self)
            
            for node in nodes[::-1]:
                parent.insert(position, node)
                
    def remove_node(self):
        if parent := self.parent:
            parent.remove(self)

    def add_event_listener(self, name: str, listener: Callable[[BaseEvent], Any]) -> None:
        self.events.setdefault(name, []).append(listener)

    def remove_event_listener(self, name: str, listener: Callable[[BaseEvent], Any]):
        if events := self.events.get(name, None):
            events.remove(listener)

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

    def set_attribute(self, name: str, value: Any):
        match name:
            case "font_size":
                self.node_style.font_size = value
            case "spacing":
                self.style = attrs.evolve(self.style, gap=value)
            case "foreground":
                self.node_style.foreground = value
            case "background":
                self.node_style.background = value
            case "padding":
                self.style = attrs.evolve(self.style, padding=value)
            case _:
                raise NotImplementedError(name)
        
    def get_attribute(self, name: str) -> Any | None:
        match name:
            case "font_size":
                return self.node_style.font_size
            case "spacing":
                return self.style.gap
            case "foreground":
                return self.node_style.foreground
            case "background":
                return self.node_style.background
            case "padding":
                return self.style.padding
            case _:
                raise NotImplementedError

    def remove_attribute(self, name: str):
        match name:
            case "font_size":
                self.node_style.font_size = None
            case "spacing":
                self._style = attrs.evolve(self.style, gap=0.0)
            case "foreground":
                self.node_style.foreground = None
            case "background":
                self.node_style.background = None
            case "padding":
                self._style = attrs.evolve(self.style, padding=0.0)
            case _:
                raise NotImplementedError

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
        inner_box = self.get_box(Edge.PADDING, relative=False)
        radii = self.node_style.border_radius

        if self.style.border.left.to_pts() == self.style.border.top.to_pts() == self.style.border.right.to_pts() == self.style.border.bottom.to_pts() == 0.0:
            rrect = skia.RRect()
            tl = (radii.topleft.to_pts(inner_box.width), radii.topleft.to_pts(inner_box.height))
            tr = (radii.topright.to_pts(inner_box.width), radii.topright.to_pts(inner_box.height))
            br = (radii.bottomright.to_pts(inner_box.width), radii.bottomright.to_pts(inner_box.height))
            bl = (radii.bottomleft.to_pts(inner_box.width), radii.bottomleft.to_pts(inner_box.height))

            rrect.setRectRadii(skia.Rect(inner_box.x, inner_box.y, inner_box.x + inner_box.width, inner_box.y + inner_box.height), [tl, tr, br, bl])

            canvas.drawRRect(rrect, skia.Paint(AntiAlias=True, Color=(self.get_background_style() or CLEAR).inner))
        else:
            canvas.drawRect(skia.Rect(inner_box.x, inner_box.y, inner_box.x + inner_box.width, inner_box.y + inner_box.height), skia.Paint(Color=(self.get_background_style() or CLEAR).inner))

        # borders
        border = self.style.border

        # top
        canvas.drawRect(skia.Rect(inner_box.x, box.y, inner_box.x + inner_box.width, inner_box.y), skia.Paint(Color=(self.node_style.border_color or BLACK).inner))

        # left
        canvas.drawRect(skia.Rect(box.x, box.y + border.top.to_pts(box.height), inner_box.x, inner_box.y + inner_box.height), skia.Paint(Color=(self.node_style.border_color or BLACK).inner))

        # right
        canvas.drawRect(skia.Rect(inner_box.x + inner_box.width, box.y + border.top.to_pts(box.height), box.x + box.width, inner_box.y + inner_box.height), skia.Paint(Color=(self.node_style.border_color or BLACK).inner))

        # bottom
        canvas.drawRect(skia.Rect(inner_box.x, inner_box.y + inner_box.height, inner_box.x + inner_box.width, box.y + box.height), skia.Paint(Color=(self.node_style.border_color or BLACK).inner))

        # border corners
        tl = (radii.topleft.to_pts(box.width), radii.topleft.to_pts(box.height))
        tr = (radii.topright.to_pts(box.width), radii.topright.to_pts(box.height))
        br = (radii.bottomright.to_pts(box.width), radii.bottomright.to_pts(box.height))
        bl = (radii.bottomleft.to_pts(box.width), radii.bottomleft.to_pts(box.height))

        # top left
        rrect = skia.RRect()
        rrect.setRectRadii(skia.Rect(box.x, box.y, inner_box.x, inner_box.y), [tl, (0, 0), (0, 0), (0, 0)])
        canvas.drawRRect(rrect, skia.Paint(AntiAlias=True, Color=(self.node_style.border_color or BLACK).inner))

        # top right
        rrect = skia.RRect()
        rrect.setRectRadii(skia.Rect(inner_box.x + inner_box.width, box.y, box.x + box.width, inner_box.y), [(0, 0), tr, (0, 0), (0, 0)])
        canvas.drawRRect(rrect, skia.Paint(AntiAlias=True, Color=(self.node_style.border_color or BLACK).inner))

        # bottom right
        rrect = skia.RRect()
        rrect.setRectRadii(skia.Rect(inner_box.x + inner_box.width, inner_box.y + inner_box.height, box.x + box.width, box.y + box.height), [(0, 0), (0, 0), br, (0, 0)])
        canvas.drawRRect(rrect, skia.Paint(AntiAlias=True, Color=(self.node_style.border_color or BLACK).inner))

        # bottom left
        rrect = skia.RRect()
        rrect.setRectRadii(skia.Rect(box.x, inner_box.y + inner_box.height, inner_box.x, box.y + box.height), [(0, 0), (0, 0), (0, 0), bl])
        canvas.drawRRect(rrect, skia.Paint(AntiAlias=True, Color=(self.node_style.border_color or BLACK).inner))

    def draw(self, canvas: Any) -> stretchable.Box:
        raise NotImplementedError

def measure_node(node: Node, size: SizePoints, available: SizeAvailableSpace):
    if isinstance(node, TextNode):
        if font_size := node.get_font_size():
            node.font.setSize(font_size)

        height = node.font.getSize()
        width = node.font.measureText(node.text)
        
        print(width, height)

        return SizePoints(width * PT, height * PT)
    
    else:
        return SizePoints(NAN, NAN)

class Node(RootNode):
    def __init__(self, id: Any | None = None, *, layout: Layout | None = None, style: Style | None = None, hover_style: Style | None = None, events: dict[str, list[Callable[[Any], Any]]] | None = None):
        super().__init__(id, layout=layout, style=style, hover_style=hover_style, events=events)
        
        self.measure = measure_node

    def draw(self, canvas: Any) -> stretchable.Box:
        box = self.get_box(relative=False)
        self.draw_bg(box, canvas)

        return box

class TextNode(Node):
    def __init__(
            self,
            text: str,
            id: Any | None = None,
            layout: stretchable.Style | None = None,
            style: Style | None = None,
            hover_style: Style | None = None
        ):
        super().__init__(id=id, layout=layout, style=style, hover_style=hover_style)

        self.font = skia.Font()

        self.text = text

    def draw(self, canvas: Any) -> stretchable.Box:
        box = self.get_box(relative=False)

        metrics = self.font.getMetrics()

        self.draw_bg(box, canvas)

        canvas.drawSimpleText(self.text, box.x, box.y - metrics.fAscent, self.font, skia.Paint(AntiAlias=True, Color=(self.get_foreground_style() or BLACK).inner))

        return box

class Stack(Node):
    def __init__(self, direction: FlexDirection, id: Any | None = None, *, layout: Layout | None = None, style: Style | None = None, hover_style: Style | None = None, events: dict[str, list[Callable[[Any], Any]]] | None = None):
        layout = layout or Layout()
        
        layout = attrs.evolve(layout, flex_direction = layout.flex_direction or direction)
        
        super().__init__(id, layout=layout, style=style, hover_style=hover_style, events=events)

class HStack(Stack):
    def __init__(self, id: Any | None = None, *, layout: Layout | None = None, style: Style | None = None, hover_style: Style | None = None, events: dict[str, list[Callable[[Any], Any]]] | None = None):        
        super().__init__(FlexDirection.ROW, id, layout=layout, style=style, hover_style=hover_style, events=events)
        
class VStack(Stack):
    def __init__(self, id: Any | None = None, *, layout: Layout | None = None, style: Style | None = None, hover_style: Style | None = None, events: dict[str, list[Callable[[Any], Any]]] | None = None):        
        super().__init__(FlexDirection.COLUMN, id, layout=layout, style=style, hover_style=hover_style, events=events)
        
class Button(Node):
    def __init__(self, id: Any | None = None, *, layout: Layout | None = None, style: Style | None = None, hover_style: Style | None = None, events: dict[str, list[Callable[[Any], Any]]] | None = None):
        style = style or Style()
        style = attrs.evolve(style,
            background = style.background or Color.rgb(0x585858),
            border_radius = style.border_radius or 4
        )
        
        layout = layout or Layout()
        layout = attrs.evolve(layout,
            padding = layout.padding or RectPointsPercent(top=1, bottom=1, left=6, right=6)
        )
            
        hover_style = hover_style or Style()        
        hover_style = attrs.evolve(hover_style,
            background = hover_style.background or Color.rgb(0x686868)
        )
        
        super().__init__(id, layout=layout, style=style, hover_style=hover_style, events=events)
