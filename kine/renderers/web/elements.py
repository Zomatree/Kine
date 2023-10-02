from typing import TypeVar, TypedDict, Callable, Any, cast
from typing_extensions import Unpack

from ...elements import Element as BaseElement, CGI

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
    "html",
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
    "object",
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

class ElementArgs(TypedDict, total=False):
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

    extras: dict[
        str, Any
    ]  # typeddict doesnt have to way to have extra none-static keys so i have to shove them in there own key


mapped_attributes = {"prevent_default": "kine-prevent-default", "class_": "class", "for_": "for", "is_": "is"}


class InnnerElement(BaseElement):
    def __init__(self, **attributes: Unpack[ElementArgs]):
        unrolled_attributes = cast(dict[str, Any], attributes) | attributes.pop("extras", cast(dict[str, Any], {}))
        remapped_attributes = {mapped_attributes.get(k, k): v for k, v in unrolled_attributes.items()}

        super().__init__(**remapped_attributes)

class Element(CGI, InnnerElement):
    pass

class base(Element):
    pass


class head(Element):
    pass


class link(Element):
    pass


class title(Element):
    pass


class body(Element):
    pass


class address(Element):
    pass


class article(Element):
    pass


class input(Element):
    pass


class button(Element):
    pass


class h1(Element):
    pass


class h2(Element):
    pass


class h3(Element):
    pass


class h4(Element):
    pass


class h5(Element):
    pass


class a(Element):
    pass


class abbr(Element):
    pass


class area(Element):
    pass


class aside(Element):
    pass


class audio(Element):
    pass


class b(Element):
    pass


class bdi(Element):
    pass


class bdo(Element):
    pass


class blockquote(Element):
    pass


class br(Element):
    pass


class canvas(Element):
    pass


class caption(Element):
    pass


class cite(Element):
    pass


class code(Element):
    pass


class col(Element):
    pass


class colgroup(Element):
    pass


class data(Element):
    pass


class datalist(Element):
    pass


class dd(Element):
    pass


del_ = type("del", (Element,), {})


class details(Element):
    pass


class dfn(Element):
    pass


class dialog(Element):
    pass


class dl(Element):
    pass


class dt(Element):
    pass


class em(Element):
    pass


class embed(Element):
    pass


class fieldset(Element):
    pass


class figcaption(Element):
    pass


class figure(Element):
    pass


class footer(Element):
    pass


class form(Element):
    pass


class header(Element):
    pass


class hgroup(Element):
    pass


class hr(Element):
    pass


class i(Element):
    pass


class iframe(Element):
    pass


class img(Element):
    pass


class ins(Element):
    pass


class kbd(Element):
    pass


class label(Element):
    pass


class legend(Element):
    pass


class li(Element):
    pass


map_ = type("map", (Element,), {})


class mark(Element):
    pass


class menu(Element):
    pass


class meta(Element):
    pass


class meter(Element):
    pass


class nav(Element):
    pass


class noscript(Element):
    pass


class object(Element):
    pass


class ol(Element):
    pass


class optgroup(Element):
    pass


class option(Element):
    pass


class output(Element):
    pass


class p(Element):
    pass


class picture(Element):
    pass


class pre(Element):
    pass


class progress(Element):
    pass


class q(Element):
    pass


class rp(Element):
    pass


class rt(Element):
    pass


class ruby(Element):
    pass


class s(Element):
    pass


class samp(Element):
    pass


class script(Element):
    pass


class section(Element):
    pass


class select(Element):
    pass


class slot(Element):
    pass


class small(Element):
    pass


class source(Element):
    pass


class span(Element):
    pass


class strong(Element):
    pass


class style(Element):
    pass


class sub(Element):
    pass


class summary(Element):
    pass


class sup(Element):
    pass


class table(Element):
    pass


class tbody(Element):
    pass


class td(Element):
    pass


class template(Element):
    pass


class textarea(Element):
    pass


class tfoot(Element):
    pass


class thead(Element):
    pass


class time(Element):
    pass


class tr(Element):
    pass


class track(Element):
    pass


class u(Element):
    pass


class ul(Element):
    pass


class var(Element):
    pass


class video(Element):
    pass


class wbr(Element):
    pass


class div(Element):
    pass

def el(name: str, /, **kwargs: Unpack[ElementArgs]) -> Element:
    el = Element(**kwargs)
    el.name = name

    return el

class html:
    x_p = p

    @staticmethod
    def rawhtml(text: str) -> str:
        return text