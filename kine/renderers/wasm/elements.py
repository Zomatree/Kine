from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar, TypedDict, Callable, Any, cast
from typing_extensions import Unpack

import js

from ...elements import Element as BaseElement, CGI

if TYPE_CHECKING:
    from ...hooks import UseRef

E = TypeVar("E", bound=js.Element)

__all__: tuple[str, ...] = (
    "InputEvent",
    "ElementArgs",
    "Element",
    "base",
    "head",
    "link",
    "title",
    "body",
    "address",
    "article",
    "input",
    "button",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "a",
    "abbr",
    "area",
    "aside",
    "audio",
    "b",
    "bdi",
    "bdo",
    "blockquote",
    "br",
    "canvas",
    "caption",
    "caption",
    "cite",
    "code",
    "col",
    "colgroup",
    "data",
    "datalist",
    "dd",
    "del_",
    "details",
    "dfn",
    "dl",
    "dt",
    "em",
    "embed",
    "fieldset",
    "figcaption",
    "figure",
    "footer",
    "form",
    "header",
    "hgroup",
    "hr",
    "i",
    "iframe",
    "img",
    "ins",
    "kbd",
    "label",
    "legend",
    "li",
    "map_",
    "mark",
    "menu",
    "meta",
    "meter",
    "nav",
    "noscript",
    "_object",
    "ol",
    "optgroup",
    "option",
    "output",
    "p",
    "picture",
    "pre",
    "progress",
    "q",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "script",
    "section",
    "select",
    "slot",
    "small",
    "source",
    "span",
    "strong",
    "style",
    "sub",
    "summary",
    "sup",
    "table",
    "tbody",
    "td",
    "template",
    "textarea",
    "tfoot",
    "thead",
    "time",
    "tr",
    "track",
    "u",
    "ul",
    "var",
    "video",
    "wbr",
    "div",
)

T = TypeVar("T")

class CopyEvent(TypedDict):
    pass

class InputEvent(TypedDict):
    value: str
    values: dict[str, str]

class CompositionEvent(TypedDict):
    data: str

class KeyEvent(TypedDict):
    char_code: int
    key: str
    alt_key: bool
    ctrl_key: bool
    meta_key: bool
    shift_key: bool
    location: int
    repeat: bool
    which: int
    code: str

class FocusEvent(TypedDict):
    pass

class ChangeEvent(TypedDict):
    value: str
    values: dict[str, str]

class MouseEvent(TypedDict):
    alt_key: bool
    button: int
    buttons: int
    client_x: int
    client_y: int
    ctrl_key: bool
    meta_key: bool
    offset_x: int
    offset_y: int
    page_x: int
    page_y: int
    screen_x: int
    screen_y: int
    shift_key: int

class PointerEvent(TypedDict):
    alt_key: bool
    button: int
    buttons: int
    client_x: int
    client_y: int
    ctrl_key: bool
    meta_key: bool
    offset_x: int
    offset_y: int
    page_x: int
    page_y: int
    screen_x: int
    screen_y: int
    shift_key: int
    pointer_id: int
    width: int
    height: int
    pressure: int
    tangential_pressure: int
    tilt_x: int
    tilt_y: int
    twist: int
    pointer_type: str
    is_primary: bool

class SelectEvent(TypedDict):
    pass

class TouchEvent(TypedDict):
    alt_key: bool
    ctrl_key: bool
    meta_key: bool
    shift_key: bool

class ScrollEvent(TypedDict):
    pass

class WheelEvent(TypedDict):
    delta_x: int
    delta_y: int
    delta_z: int
    delta_move: int
class AnimationEvent(TypedDict):
    animation_name: str
    elapsed_time: int
    pseudo_element: str

class TransitionEvent(TypedDict):
    property_name: str
    elapsed_time: int
    pseudo_element: str

class VideoEvent(TypedDict):
    pass

class ToggleEvent(TypedDict):
    pass

EventCallback = Callable[[T], Any]

class ElementArgs(TypedDict, Generic[E], total=False):
    accesskey: str
    autocapitalize: str
    autofocus: str
    class_: str
    contenteditable: str
    dir: str
    draggable: str
    enterkeyhint: str
    exportparts: str
    hidden: str
    id: str
    inert: str
    inputmode: str
    is_: str
    itemid: str
    itemprop: str
    itemref: str
    itemscope: str
    itemtype: str
    lang: str
    nonce: str
    part: str
    spellcheck: str
    style: str
    tabindex: str
    title: str
    translate: str
    accept: str
    autocomplete: str
    capture: str
    crossorigin: str
    disabled: str
    elementtiming: str
    for_: str
    max: str
    maxlength: str
    minlength: str
    multiple: str
    pattern: str
    readonly: str
    rel: str
    required: str
    size: str
    step: str
    key: str
    name: str

    type: str
    href: str
    prevent_default: str

    oncompositionend: EventCallback[CompositionEvent]
    oncompositionstart: EventCallback[CompositionEvent]
    oncompositionupdate: EventCallback[CompositionEvent]
    onkeyup: EventCallback[KeyEvent]
    onkeydown: EventCallback[KeyEvent]
    onkeypress: EventCallback[KeyEvent]
    onchange: EventCallback[ChangeEvent]
    oninput: EventCallback[InputEvent]
    oninvalid: EventCallback[InputEvent]
    onreset: EventCallback[InputEvent]
    onsubmit: EventCallback[InputEvent]
    onclick: EventCallback[MouseEvent]
    oncontextmenu: EventCallback[MouseEvent]
    ondoubleclick: EventCallback[MouseEvent]
    ondblclick: EventCallback[MouseEvent]
    ondrag: EventCallback[MouseEvent]
    ondragend: EventCallback[MouseEvent]
    ondragenter: EventCallback[MouseEvent]
    ondragexit: EventCallback[MouseEvent]
    ondragleave: EventCallback[MouseEvent]
    ondragover: EventCallback[MouseEvent]
    ondragstart: EventCallback[MouseEvent]
    ondrop: EventCallback[MouseEvent]
    onmousedown: EventCallback[MouseEvent]
    onmouseenter: EventCallback[MouseEvent]
    onmouseleave: EventCallback[MouseEvent]
    onmousemove: EventCallback[MouseEvent]
    onmouseout: EventCallback[MouseEvent]
    onmouseover: EventCallback[MouseEvent]
    onmouseup: EventCallback[MouseEvent]
    onpointerdown: EventCallback[PointerEvent]
    onpointermove: EventCallback[PointerEvent]
    onpointerup: EventCallback[PointerEvent]
    onpointercancel: EventCallback[PointerEvent]
    ongotpointercapture: EventCallback[PointerEvent]
    onlostpointercapture: EventCallback[PointerEvent]
    onpointerenter: EventCallback[PointerEvent]
    onpointerleave: EventCallback[PointerEvent]
    onpointerover: EventCallback[PointerEvent]
    onpointerout: EventCallback[PointerEvent]
    ontouchcancel: EventCallback[TouchEvent]
    ontouchend: EventCallback[TouchEvent]
    ontouchmove: EventCallback[TouchEvent]
    ontouchstart: EventCallback[TouchEvent]
    onwheel: EventCallback[WheelEvent]
    ontransitionend: EventCallback[TransitionEvent]

    ref:  UseRef[E]

    extras: dict[
        str, Any
    ]  # typeddict doesnt have to way to have extra none-static keys so i have to shove them in there own key


mapped_attributes = {"prevent_default": "kine-prevent-default", "class_": "class", "for_": "for", "is_": "is"}


class Element(BaseElement, Generic[E]):
    def __init__(self, **attributes: Unpack[ElementArgs[E]]):
        ref = attributes.pop("ref", None)

        unrolled_attributes = cast(dict[str, Any], attributes) | attributes.pop("extras", cast(dict[str, Any], {}))
        remapped_attributes = {mapped_attributes.get(k, k): v for k, v in unrolled_attributes.items()}

        super().__init__(**remapped_attributes)

        self.ref = ref

class base(CGI, Element[js.HTMLBaseElement]):
    pass


class head(CGI, Element[js.HTMLHeadElement]):
    pass


class link(CGI, Element[js.HTMLLinkElement]):
    pass


class title(CGI, Element[js.HTMLTitleElement]):
    pass


class body(CGI, Element[js.HTMLBodyElement]):
    pass


class address(CGI, Element[js.HTMLElement]):
    pass


class article(CGI, Element[js.HTMLElement]):
    pass


class input(CGI, Element[js.HTMLInputElement]):
    pass


class button(CGI, Element[js.HTMLButtonElement]):
    pass


class h1(CGI, Element[js.HTMLHeadingElement]):
    pass


class h2(CGI, Element[js.HTMLHeadingElement]):
    pass


class h3(CGI, Element[js.HTMLHeadingElement]):
    pass


class h4(CGI, Element[js.HTMLHeadingElement]):
    pass


class h5(CGI, Element[js.HTMLHeadingElement]):
    pass


class a(CGI, Element[js.HTMLElement]):
    pass


class abbr(CGI, Element[js.HTMLElement]):
    pass


class area(CGI, Element[js.HTMLAreaElement]):
    pass


class aside(CGI, Element[js.HTMLElement]):
    pass


class audio(CGI, Element[js.HTMLAudioElement]):
    pass


class b(CGI, Element[js.HTMLElement]):
    pass


class bdi(CGI, Element[js.HTMLElement]):
    pass


class bdo(CGI, Element[js.HTMLElement]):
    pass


class blockquote(CGI, Element[js.HTMLElement]):
    pass


class br(CGI, Element[js.HTMLBRElement]):
    pass


class canvas(CGI, Element[js.HTMLCanvasElement]):
    pass


class caption(CGI, Element[js.HTMLElement]):
    pass


class cite(CGI, Element[js.HTMLElement]):
    pass


class code(CGI, Element[js.HTMLElement]):
    pass


class col(CGI, Element[js.HTMLElement]):
    pass


class colgroup(CGI, Element[js.HTMLElement]):
    pass


class data(CGI, Element[js.HTMLDataElement]):
    pass


class datalist(CGI, Element[js.HTMLDataListElement]):
    pass


class dd(CGI, Element[js.HTMLElement]):
    pass

class del_(CGI, Element[js.HTMLElement]):
    name = "del"

class details(CGI, Element[js.HTMLDetailsElement]):
    pass


class dfn(CGI, Element[js.HTMLElement]):
    pass


class dialog(CGI, Element[js.HTMLDialogElement]):
    pass


class dl(CGI, Element[js.HTMLElement]):
    pass


class dt(CGI, Element[js.HTMLElement]):
    pass


class em(CGI, Element[js.HTMLElement]):
    pass


class embed(CGI, Element[js.HTMLEmbedElement]):
    pass


class fieldset(CGI, Element[js.HTMLFieldSetElement]):
    pass


class figcaption(CGI, Element[js.HTMLElement]):
    pass


class figure(CGI, Element[js.HTMLElement]):
    pass


class footer(CGI, Element[js.HTMLElement]):
    pass


class form(CGI, Element[js.HTMLFormElement]):
    pass


class header(CGI, Element[js.HTMLElement]):
    pass


class hgroup(CGI, Element[js.HTMLElement]):
    pass


class hr(CGI, Element[js.HTMLHRElement]):
    pass


class i(CGI, Element[js.HTMLElement]):
    pass


class iframe(CGI, Element[js.HTMLIFrameElement]):
    pass


class img(CGI, Element[js.HTMLImageElement]):
    pass


class ins(CGI, Element[js.HTMLElement]):
    pass


class kbd(CGI, Element[js.HTMLElement]):
    pass


class label(CGI, Element[js.HTMLLabelElement]):
    pass


class legend(CGI, Element[js.HTMLLegendElement]):
    pass


class li(CGI, Element[js.HTMLLIElement]):
    pass


class map_(CGI, Element[js.HTMLMapElement]):
    name = "map"

class mark(CGI, Element[js.HTMLElement]):
    pass


class menu(CGI, Element[js.HTMLMenuElement]):
    pass


class meta(CGI, Element[js.HTMLMetaElement]):
    pass


class meter(CGI, Element[js.HTMLMeterElement]):
    pass


class nav(CGI, Element[js.HTMLElement]):
    pass


class noscript(CGI, Element[js.HTMLElement]):
    pass


class _object(CGI, Element[js.HTMLObjectElement]):
    pass


class ol(CGI, Element[js.HTMLOListElement]):
    pass


class optgroup(CGI, Element[js.HTMLOptGroupElement]):
    pass


class option(CGI, Element[js.HTMLOptionElement]):
    pass


class output(CGI, Element[js.HTMLOutputElement]):
    pass


class p(CGI, Element[js.HTMLParagraphElement]):
    pass


class picture(CGI, Element[js.HTMLPictureElement]):
    pass


class pre(CGI, Element[js.HTMLPreElement]):
    pass


class progress(CGI, Element[js.HTMLProgressElement]):
    pass


class q(CGI, Element[js.HTMLQuoteElement]):
    pass


class rp(CGI, Element[js.HTMLElement]):
    pass


class rt(CGI, Element[js.HTMLElement]):
    pass


class ruby(CGI, Element[js.HTMLElement]):
    pass


class s(CGI, Element[js.HTMLElement]):
    pass


class samp(CGI, Element[js.HTMLElement]):
    pass


class script(CGI, Element[js.HTMLScriptElement]):
    pass


class section(CGI, Element[js.HTMLElement]):
    pass


class select(CGI, Element[js.HTMLSelectElement]):
    pass


class slot(CGI, Element[js.HTMLSlotElement]):
    pass


class small(CGI, Element[js.HTMLElement]):
    pass


class source(CGI, Element[js.HTMLSourceElement]):
    pass


class span(CGI, Element[js.HTMLSpanElement]):
    pass


class strong(CGI, Element[js.HTMLElement]):
    pass


class style(CGI, Element[js.HTMLStyleElement]):
    pass


class sub(CGI, Element[js.HTMLElement]):
    pass


class summary(CGI, Element[js.HTMLElement]):
    pass


class sup(CGI, Element[js.HTMLElement]):
    pass


class table(CGI, Element[js.HTMLTableElement]):
    pass


class tbody(CGI, Element[js.HTMLElement]):
    pass


class td(CGI, Element[js.HTMLTableCellElement]):
    pass


class template(CGI, Element[js.HTMLTemplateElement]):
    pass


class textarea(CGI, Element[js.HTMLTextAreaElement]):
    pass


class tfoot(CGI, Element[js.HTMLTableSectionElement]):
    pass


class thead(CGI, Element[js.HTMLTableSectionElement]):
    pass


class time(CGI, Element[js.HTMLTimeElement]):
    pass


class tr(CGI, Element[js.HTMLTableRowElement]):
    pass


class track(CGI, Element[js.HTMLTrackElement]):
    pass


class u(CGI, Element[js.HTMLElement]):
    pass


class ul(CGI, Element[js.HTMLUListElement]):
    pass


class var(CGI, Element[js.HTMLElement]):
    pass


class video(CGI, Element[js.HTMLVideoElement]):
    pass


class wbr(CGI, Element[js.HTMLElement]):
    pass


class div(CGI, Element[js.HTMLDivElement]):
    pass

def el(name: str, /, **kwargs: Unpack[ElementArgs[E]]) -> Element[E]:
    el = Element(**kwargs)
    el.name = name

    return el
