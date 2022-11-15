from typing import Callable, TypedDict, Any
from typing_extensions import Unpack

from ...elements import Element as BaseElement, CGI

class ElementArgs(TypedDict, total=False):
    onclick: Callable[[Any], None]

class Element(BaseElement):
    def __init__(self, **attributes: Unpack[ElementArgs]):
        super().__init__(**attributes)

class static(CGI, Element): pass
class container(CGI, Element): pass
class button(CGI, Element): pass
class virtual(CGI, Element): pass
class horizontal(CGI, Element): pass
class header(CGI, Element): pass
class footer(CGI, Element): pass
