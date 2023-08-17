from __future__ import annotations

from typing import TYPE_CHECKING, Generic, ParamSpec, TypedDict, Any, Callable
import asyncio

from ... import ComponentFunction, messages, diff
from ...dom import VirtualDom, ElementId

from ..web_elements import *

P = ParamSpec("P")


class GlobalEvent(TypedDict):
    callback: Callable[..., Any]
    active: int


class App(Generic[P]):
    def __init__(self, app: ComponentFunction[P]) -> None:
        import js

        self.dom = VirtualDom(app)
        self.globals: dict[str, GlobalEvent] = {}
        self.locals: dict[str, dict[str, Callable[..., Any]]] = {}
        self.event_queue = asyncio.Queue[Any]()

        main = js.document.getElementById("main")

        if not main:
            raise Exception("No element with id of main")

        self.nodes: dict[ElementId, js.Element | js.Text] = {ElementId(0): main}

    async def start(self):
        edits = self.dom.rebuild()
        self.calculate_diffs(edits)

        while True:
            futs = await asyncio.wait(
                [
                    asyncio.ensure_future(self.dom.wait_for_work()),
                    asyncio.ensure_future(self.event_queue.get()),
                ],
                return_when=asyncio.FIRST_COMPLETED,
            )

            dones, pending = futs

            for task in pending:
                task.cancel()

            for done in dones:
                if msg := done.result():
                    if msg["method"] == "user_event":
                        payload = msg["params"]
                        self.dom.handle_message(
                            messages.EventMessage(
                                scope_id=None,
                                priority=0,
                                element_id=payload["mounted_dom_id"],
                                name=payload["event"],
                                bubbles=False,
                                data=payload["contents"],
                            )
                        )

                mutations = self.dom.work_with_deadline(lambda: False)

                for mutation in mutations:
                    self.calculate_diffs(mutation)

    def calculate_diffs(self, mutation: diff.Mutations):
        import js
        from pyodide.ffi import create_proxy

        for mod in mutation.modifications:
            match mod:
                case diff.AppendChildren():
                    node = self.nodes[mod.root]

                    for child in mod.children:
                        node.appendChild(self.nodes[child])

                case diff.ReplaceWith():
                    node = self.nodes[mod.root]
                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)

                    elements = [self.nodes[id] for id in mod.nodes]
                    node.replaceWith(*elements)

                case diff.CreateElement():
                    element = js.document.createElement(mod.tag)
                    self.nodes[mod.root] = element

                case diff.CreateTextNode():
                    element = js.document.createTextNode(mod.text)
                    self.nodes[mod.root] = element

                case diff.NewEventListener():

                    def callback(event: Any):
                        target = event.target
                        if not target:
                            return

                        real_id = target.getAttribute("data-kine-id")

                        while real_id is None:
                            if target.parentElement == None:
                                return

                            target = target.parentElement
                            real_id = target.getAttribute("data-kine-id")

                        should_prevent_default = target.getAttribute("kine-prevent-default")

                        contents = self.transform_event(event)

                        if should_prevent_default == f"on{event.type}" or event.type == "submit":
                            event.preventDefault()

                        if target.tagName == "FORM" and event.type in ("submit", "input"):
                            for element in target.elements:
                                name = event.getAttribute("name")

                                if name is None:
                                    continue

                                element_type = element.getAttribute("type")

                                if element_type == "checkbox":
                                    contents["values"][name] = element.checked
                                elif element_type == "radio" and element.checked:
                                    contents["values"][name] = element.value
                                else:
                                    contents["values"] = element.value or element.textContent

                        if real_id == None:
                            return

                        self.event_queue.put_nowait(
                            {
                                "method": "user_event",
                                "params": {"event": event.type, "mounted_dom_id": int(real_id), "contents": contents},
                            }
                        )

                    proxy_func = create_proxy(callback)

                    node = self.nodes[mod.root]

                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)

                    node.setAttribute("data-kine-id", str(mod.root))

                    if self.should_bubble(mod.event_name):
                        g = self.globals.get(mod.event_name)

                        if not g:
                            self.globals[mod.event_name] = GlobalEvent(active=1, callback=proxy_func)
                            self.nodes[ElementId(0)].addEventListener(mod.event_name, proxy_func)
                        else:
                            g["active"] += 1

                    else:
                        id = node.getAttribute("data-kine-id")
                        assert id

                        local = self.locals.setdefault(id, {})

                        local[mod.event_name] = proxy_func

                        node.addEventListener(mod.event_name, proxy_func)

                case diff.SetText():
                    node = self.nodes[mod.root]
                    if TYPE_CHECKING:
                        assert isinstance(node, js.Text)
                    node.data = mod.text

                case diff.SetAttribute():
                    node = self.nodes[mod.root]

                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)

                    if mod.field == "value":
                        if TYPE_CHECKING:
                            assert isinstance(node, js.HTMLInputElement)

                        if mod.value != node.value:
                            node.value = mod.value

                    else:
                        node.setAttribute(mod.field, mod.value)

                case diff.InsertAfter():
                    node = self.nodes[mod.root]
                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)
                    elements = [self.nodes[id] for id in mod.nodes]
                    node.after(*elements)

                case diff.Remove():
                    node = self.nodes[mod.root]
                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)
                    node.remove()

                case diff.InsertBefore():
                    node = self.nodes[mod.root]
                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)
                    elements = [self.nodes[id] for id in mod.nodes]
                    node.before(*elements)

                case diff.CreatePlaceholder():
                    node = js.document.createElement("pre")

                    if TYPE_CHECKING:
                        assert isinstance(node, js.HTMLElement)

                    node.hidden = True
                    self.nodes[mod.root] = node

                case diff.RemoveAttribute():
                    node = self.nodes[mod.root]

                    if mod.field == "value":
                        if TYPE_CHECKING:
                            assert isinstance(node, js.HTMLInputElement)

                        node.value = ""
                    else:
                        if TYPE_CHECKING:
                            assert isinstance(node, js.Element)
                        node.removeAttribute(mod.field)

                case diff.RemoveEventListener():
                    node = self.nodes[mod.root]

                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)

                    node.removeAttribute("data-kine-id")

                    if self.should_bubble(mod.event_name):
                        self.globals[mod.event_name]["active"] -= 1

                        if self.globals[mod.event_name]["active"] == 0:
                            root = self.nodes[ElementId(0)]

                            if TYPE_CHECKING:
                                assert isinstance(root, js.Element)

                            root.removeEventListener(mod.event_name, self.globals[mod.event_name]["callback"])

                            del self.globals[mod.event_name]

                    else:
                        id = node.getAttribute("data-kine-id")
                        assert id is not None

                        listeners = self.locals[id]

                        handler = listeners.pop(mod.event_name)

                        if len(listeners) == 0:
                            del self.locals[id]

                        node.removeEventListener(mod.event_name, handler)

                case diff.RemoveAllChildren():
                    node = self.nodes[mod.root]

                    if TYPE_CHECKING:
                        assert isinstance(node, js.Element)

                    node.replaceChildren()

    def should_bubble(self, event_name: str) -> bool:
        return event_name in [
            "copy",
            "cut",
            "paste",
            "compositionend",
            "compositionstart",
            "compositionupdate",
            "keydown",
            "keypress",
            "keyup",
            "focusout",
            "focusin",
            "change",
            "input",
            "invalid",
            "reset",
            "submit",
            "click",
            "contextmenu",
            "doubleclick",
            "dblclick",
            "drag",
            "dragend",
            "dragleave",
            "dragover",
            "dragstart",
            "drop",
            "mousedown",
            "mousemove",
            "mouseout",
            "mouseover",
            "mouseup",
            "pointerdown",
            "pointermove",
            "pointerup",
            "pointercancel",
            "gotpointercapture",
            "lostpointercapture",
            "pointerover",
            "pointerout",
            "select",
            "touchcancel",
            "touchend",
            "touchmove",
            "touchstart",
            "wheel",
            "encrypted",
            "animationstart",
            "animationend",
            "animationiteration",
            "transitionend",
            "toggle",
        ]

    # i frankly cannot be bothered to re-type all of js's events to python
    def transform_event(self, event: Any) -> dict[str, Any]:
        match event.type:
            case "compositionend" | "compositionstart" | "compositionupdate":
                return {"data": event.data}
            case "keyup" | "keydown" | "keypress":
                return {
                    "char_code": event.charCode,
                    "key": event.key,
                    "alt_key": event.altKey,
                    "ctrl_key": event.ctrlKey,
                    "meta_key": event.metaKey,
                    "key_code": event.keyCode,
                    "shift_key": event.shiftKey,
                    "location": event.location,
                    "repeat": event.repeat,
                    "which": event.which,
                    "code": event.code,
                }
            case "change":
                if event.target.type in ("checkbox", "radio"):
                    value = event.target.checked
                else:
                    value = event.target.value or event.target.textContent

                return {"value": value, "values": {}}
            case "input" | "invalid" | "reset" | "submit":
                value = event.target.value or event.target.textContent

                if event.target.type == "checkbox":
                    value = event.target.checked

                return {"value": value, "values": {}}
            case "click" | "contextmenu" | "doubleclick" | "dblclick" | "drag" | "dragend" | "dragenter" | "dragexit" | "dragleave" | "dragover" | "dragstart" | "drop" | "mousedown" | "mouseenter" | "mouseleave" | "mousemove" | "mouseout" | "mouseover" | "mouseup":
                return {
                    "alt_key": event.altKey,
                    "button": event.button,
                    "buttons": event.buttons,
                    "client_x": event.clientX,
                    "client_y": event.clientY,
                    "ctrl_key": event.ctrlKey,
                    "meta_key": event.metaKey,
                    "offset_x": event.offsetX,
                    "offset_y": event.offsetY,
                    "page_x": event.pageX,
                    "page_y": event.pageY,
                    "screen_x": event.screenX,
                    "screen_y": event.screenY,
                    "shift_key": event.shiftKey,
                }
            case "pointerdown" | "pointermove" | "pointerup" | "pointercancel" | "gotpointercapture" | "lostpointercapture" | "pointerenter" | "pointerleave" | "pointerover" | "pointerout":
                return {
                    "alt_key": event.altKey,
                    "button": event.button,
                    "buttons": event.buttons,
                    "client_x": event.clientX,
                    "client_y": event.clientY,
                    "ctrl_key": event.ctrlKey,
                    "meta_key": event.metaKey,
                    "page_x": event.pageX,
                    "page_y": event.pageY,
                    "screen_x": event.screenX,
                    "screen_y": event.screenY,
                    "shift_key": event.shiftKey,
                    "pointer_id": event.pointerId,
                    "width": event.width,
                    "height": event.height,
                    "pressure": event.pressure,
                    "tangential_pressure": event.tangentialPressure,
                    "tilt_x": event.tiltX,
                    "tilt_y": event.tiltY,
                    "twist": event.twist,
                    "pointer_type": event.pointerType,
                    "is_primary": event.isPrimary,
                }
            case "touchcancel" | "touchend" | "touchmove" | "touchstart":
                return {
                    "alt_key": event.altKey,
                    "ctrl_key": event.ctrlKey,
                    "meta_key": event.metaKey,
                    "shift_key": event.shiftKey,
                }
            case "wheel":
                return {
                    "animation_name": event.animationName,
                    "elapsed_time": event.elapsedTime,
                    "pseudo_element": event.pseudoElement,
                }
            case "transitionend":
                return {
                    "property_name": event.propertyName,
                    "elapsed_time": event.elapsedTime,
                    "pseudo_element": event.pseudoElement,
                }
            case _:
                return {}


async def start_wasm(app_func: ComponentFunction[P]):
    app = App(app_func)
    await app.start()
