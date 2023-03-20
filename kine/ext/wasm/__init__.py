from ... import component, Scope
from ...renderers.web_elements import *
from typing import ParamSpec
import js
import pyodide.ffi

__all__ = ("UseRouter", "use_router", "link", "route", "router")


P = ParamSpec("P")


class UseRouter:
    def __init__(self, cx: Scope):
        self.scope = cx
        self.current_route = js.document.location.pathname
        self.route_parameters: dict[str, str] = {}

    def push_route(self, route: str):
        self.current_route = route
        js.window.history.pushState(pyodide.ffi.to_js({}), "", route)

        self.scope.root_scope().schedule_update()

    def split_route(self, route: str) -> list[str]:
        return route.removeprefix("/").removeprefix("/").split("/")

    def parse_route(self, parts: list[str]) -> list[tuple[bool, str]]:
        output: list[tuple[bool, str]] = []

        for part in parts:
            if part.startswith(":"):
                output.append((True, part[1:]))
            else:
                output.append((False, part))

        return output

    def matches_route(self, route: str) -> tuple[bool, dict[str, str]]:
        current_route = self.split_route(self.current_route)
        route_parts = self.parse_route(self.split_route(route))
        dynamic_parts: dict[str, str] = {}

        if len(current_route) != len(route_parts):
            return False, dynamic_parts

        for current_part, (dynamic, match_part) in zip(current_route, route_parts):
            if dynamic:
                dynamic_parts[match_part] = current_part

            elif current_part != match_part:
                return False, dynamic_parts

        return True, dynamic_parts


def use_router(cx: Scope) -> UseRouter:
    try:
        return cx.consume_context(UseRouter)
    except LookupError as e:
        e.add_note("No router found, make sure to wrap your root component in the `router` component.")
        raise e

@component
def link(cx: Scope, route: str):
    router = use_router(cx)

    return cx.render(a(
        href=route,
        prevent_default="onclick",
        onclick=lambda _: router.push_route(route)
    )[
        cx.children
    ])


@component
def route(cx: Scope, route: str):
    router = cx.consume_context(UseRouter)

    matches, dynamic_parts = router.matches_route(route)

    if matches:
        router.route_parameters = dynamic_parts
        children = cx.children
    else:
        children = ()

    return cx.render(div[children])


@component
def router(cx: Scope):
    cx.use_hook(lambda: cx.provide_context(UseRouter(cx)))

    return cx.render(div[cx.children])
