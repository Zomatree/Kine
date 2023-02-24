from typing import TypedDict, Callable, Any, cast
from typing_extensions import Unpack

from ..elements import Element as BaseElement, CGI

class InputEvent(TypedDict):
    value: str
    values: dict[str, str]

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
    inputmode: str
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

    type: str
    href: str
    prevent_default: str

    onclick: Callable[[Any], Any]
    oninput: Callable[[InputEvent], Any]

    extras: dict[
        str, Any
    ]  # typeddict doesnt have to way to have extra none-static keys so i have to shove them in there own key


mapped_attributes = {"prevent_default": "kine-prevent-default", "class_": "class"}


class Element(BaseElement):
    def __init__(self, **attributes: Unpack[ElementArgs]):
        unrolled_attributes = cast(dict[str, Any], attributes) | attributes.pop("extras", cast(dict[str, Any], {}))
        remapped_attributes = {mapped_attributes.get(k, k): v for k, v in unrolled_attributes.items()}

        super().__init__(**remapped_attributes)


class base(CGI, Element):
    pass


class head(CGI, Element):
    pass


class link(CGI, Element):
    pass


class title(CGI, Element):
    pass


class body(CGI, Element):
    pass


class adress(CGI, Element):
    pass


class article(CGI, Element):
    pass


class input(CGI, Element):
    pass


class button(CGI, Element):
    pass


class h1(CGI, Element):
    pass


class h2(CGI, Element):
    pass


class h3(CGI, Element):
    pass


class h4(CGI, Element):
    pass


class h5(CGI, Element):
    pass


class a(CGI, Element):
    pass


class abbr(CGI, Element):
    pass


class area(CGI, Element):
    pass


class aside(CGI, Element):
    pass


class audio(CGI, Element):
    pass


class b(CGI, Element):
    pass


class bdi(CGI, Element):
    pass


class bdo(CGI, Element):
    pass


class blockquote(CGI, Element):
    pass


class br(CGI, Element):
    pass


class canvas(CGI, Element):
    pass


class caption(CGI, Element):
    pass


class cite(CGI, Element):
    pass


class code(CGI, Element):
    pass


class col(CGI, Element):
    pass


class colgroup(CGI, Element):
    pass


class data(CGI, Element):
    pass


class datalist(CGI, Element):
    pass


class dd(CGI, Element):
    pass


del_ = type("del", (CGI, Element), {})


class details(CGI, Element):
    pass


class dfn(CGI, Element):
    pass


class dialog(CGI, Element):
    pass


class dl(CGI, Element):
    pass


class dt(CGI, Element):
    pass


class em(CGI, Element):
    pass


class embed(CGI, Element):
    pass


class fieldset(CGI, Element):
    pass


class figcaption(CGI, Element):
    pass


class figure(CGI, Element):
    pass


class footer(CGI, Element):
    pass


class form(CGI, Element):
    pass


class header(CGI, Element):
    pass


class hgroup(CGI, Element):
    pass


class hr(CGI, Element):
    pass


class html(CGI, Element):
    pass


class i(CGI, Element):
    pass


class iframe(CGI, Element):
    pass


class img(CGI, Element):
    pass


class ins(CGI, Element):
    pass


class kbd(CGI, Element):
    pass


class label(CGI, Element):
    pass


class legend(CGI, Element):
    pass


class li(CGI, Element):
    pass


class main(CGI, Element):
    pass


map_ = type("map", (CGI, Element), {})


class mark(CGI, Element):
    pass


class menu(CGI, Element):
    pass


class meta(CGI, Element):
    pass


class meter(CGI, Element):
    pass


class nav(CGI, Element):
    pass


class noscript(CGI, Element):
    pass


class object(CGI, Element):
    pass


class ol(CGI, Element):
    pass


class optgroup(CGI, Element):
    pass


class option(CGI, Element):
    pass


class output(CGI, Element):
    pass


class p(CGI, Element):
    pass


class picture(CGI, Element):
    pass


class pre(CGI, Element):
    pass


class progress(CGI, Element):
    pass


class q(CGI, Element):
    pass


class rp(CGI, Element):
    pass


class rt(CGI, Element):
    pass


class ruby(CGI, Element):
    pass


class s(CGI, Element):
    pass


class samp(CGI, Element):
    pass


class script(CGI, Element):
    pass


class section(CGI, Element):
    pass


class select(CGI, Element):
    pass


class slot(CGI, Element):
    pass


class small(CGI, Element):
    pass


class source(CGI, Element):
    pass


class span(CGI, Element):
    pass


class strong(CGI, Element):
    pass


class style(CGI, Element):
    pass


class sub(CGI, Element):
    pass


class summary(CGI, Element):
    pass


class sup(CGI, Element):
    pass


class table(CGI, Element):
    pass


class tbody(CGI, Element):
    pass


class td(CGI, Element):
    pass


class template(CGI, Element):
    pass


class textarea(CGI, Element):
    pass


class tfoot(CGI, Element):
    pass


class thead(CGI, Element):
    pass


class time(CGI, Element):
    pass


class tr(CGI, Element):
    pass


class track(CGI, Element):
    pass


class u(CGI, Element):
    pass


class ul(CGI, Element):
    pass


class var(CGI, Element):
    pass


class video(CGI, Element):
    pass


class wbr(CGI, Element):
    pass


class div(CGI, Element):
    pass
