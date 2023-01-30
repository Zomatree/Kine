from ... import component, Scope, ComponentFunction, Node
from ..web_elements import *
from typing import ParamSpec, cast
import js

__all__ = ("UseRouter", "use_router", "link", "route", "router")


P = ParamSpec("P")


class UseRouter:
    def __init__(self, cx: Scope):
        self.scope = cx
        self.current_route = js.document.location.pathname
        self.route_parameters: dict[str, str] = {}

    def push_route(self, route: str):
        self.current_route = route
        js.document.location.pathname = route

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
    return cx.consume_context(UseRouter)

@component
def link(cx: Scope, route: str):
    return cx.render(a(
        href=route
    )[
       cx.children
    ])

@component
def route(cx: Scope, route: str):
    return cx.render(cx.children[0])

@component
def router(cx: Scope, *children: Node):
    router = cx.use_hook(lambda: cx.provide_context(UseRouter(cx)))

    filtered_children: list[Node] = []

    for child in children:
        match child:
            case ComponentFunction() if child.func == route.__wrapped__:  # type: ignore
                matches, dynamic_parts = router.matches_route(cast(str, child.args[0]))

                if matches:
                    router.route_parameters = dynamic_parts
                    filtered_children.append(child)
                else:
                    filtered_children.append(None)
            case _:
                filtered_children.append(child)

    return cx.render(div[tuple(filtered_children)])
