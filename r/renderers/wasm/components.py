from ... import component, Scope, ComponentFunction, Node
from ..web_elements import *
from typing import ParamSpec, cast
import js

P = ParamSpec("P")

class UseRouter:
    def __init__(self, cx: Scope):
        self.scope = cx
        self.current_route = js.document.location.pathname

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

    def matches_route(self, route: str) -> tuple[bool, list[str]]:
        current_route = self.split_route(self.current_route)
        route_parts = self.parse_route(self.split_route(route))
        dynamic_parts: list[str] = []
        js.console.log(str(current_route), str(route_parts))

        if len(current_route) != len(route_parts):
            return False, dynamic_parts

        for current_part, (dynamic, match_part) in zip(current_route, route_parts):
            if dynamic:
                dynamic_parts.append(match_part)
            elif current_part != match_part:
                return False, dynamic_parts

        return True, dynamic_parts


def use_router(cx: Scope) -> UseRouter:
    return cx.consume_context(UseRouter)

@component
def link(cx: Scope, route: str, children: tuple[Node[...], ...]):
    return cx.render(a(
        href=route
    )[
        children
    ])

@component
def route(cx: Scope, route: str, child: Node[P]):
    return cx.render(child)

@component
def router(cx: Scope, *children: Node[...]):
    router = cx.use_hook(lambda: cx.provide_context(UseRouter(cx)))

    filtered_children: list[Node[...]] = []

    for child in children:
        match child:
            case ComponentFunction():
                js.console.log("case 1", str(child))
                if child.func == route.__wrapped__:  # type: ignore
                    js.console.log(str(child.args))
                    if router.matches_route(cast(str, child.args[0])):
                        filtered_children.append(child)
            case _:
                js.console.log("case 2", str(child))
                filtered_children.append(child)

    return cx.render(div[tuple(filtered_children)])
