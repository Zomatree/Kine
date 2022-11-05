from typing import TypedDict, Callable, Any
from typing_extensions import Unpack

from ..elements import Element as BaseElement, CGI

class ElementArgs(TypedDict, total=False):
    id: str
    cls: str
    key: str
    type: str
    style: str
    href: str
    prevent_default: str

    onclick: Callable[[Any], None]
    oninput: Callable[[Any], None]

mapped_attributes = {
    "prevent_default": "r-prevent-default"
}

class Element(BaseElement):
    def __init__(self, **attributes: Unpack[ElementArgs]):
        remapped_attributes = {mapped_attributes.get(k, k): v for k, v in attributes.items()}
        super().__init__(**remapped_attributes)

class div(CGI, Element): pass
class p(CGI, Element): pass
class input(CGI, Element): pass
class button(CGI, Element): pass
class h1(CGI, Element): pass
class h2(CGI, Element): pass
class h3(CGI, Element): pass
class h4(CGI, Element): pass
class h5(CGI, Element): pass
class a(CGI, Element): pass
