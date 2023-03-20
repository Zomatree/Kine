from typing import Callable, TypeVar, Unpack
import random
import string

from kine import *
from kine.renderers import web_elements

T = TypeVar("T")

STYLES: dict[str, str] = {}


def styled_component(element: type, styling: str) -> Callable[..., ComponentFunction[...]]:
    random_chars = "".join(random.choices(string.ascii_lowercase, k=10))

    class_name = f"{element.__name__}_{random_chars}"

    STYLES[class_name] = styling

    @component
    def inner_compponent(cx: Scope, **kwargs: Unpack[web_elements.ElementArgs]):
        existing_classes = kwargs.get("class_", "")
        kwargs["class_"] = f"{class_name} {existing_classes}"

        return cx.render(element(**kwargs)[cx.children])

    return inner_compponent


def generate_styling() -> str:
    parts: list[str] = []

    for key, value in STYLES.items():
        parts.append(f".{key} {{{value}}}")

    return "\n".join(parts)


@component
def styled_component_provider(cx: Scope):
    styling = generate_styling()

    return cx.render(web_elements.div[web_elements.style[styling], *cx.children])
