from kine import *
from kine.renderers.web import *

import asyncio
from functools import partial
from typing import Any


@component
def screen(cx: Scope, output: str):
    return div[p[output]]


@component
def calc_button(cx: Scope, equation: UseState[str], char: str):
    return button(
        onclick=lambda _: equation.modify(lambda eq: eq + char),
    )[char]



@component
def enter_button(cx: Scope, output: UseState[str]):
    def onclick(_: Any):
        equation = output.get()
        output.set(str(eval(equation)))

    return button(onclick=onclick)["="]


@component
def app(cx: Scope):
    output = use_state(cx, lambda: "")

    btn = partial(calc_button, output)

    return div[
        screen(output.get()),
        div[
            div[btn("7"), btn("8"), btn("9"), btn("/")],
            div[btn("4"), btn("5"), btn("6"), btn("*")],
            div[btn("1"), btn("2"), btn("3"), btn("-")],
            div[btn("0"), btn("."), enter_button(output), btn("+")],
        ],
    ]



asyncio.run(start_web(app()))
