from __future__ import annotations

from typing import TYPE_CHECKING, Any, Mapping, ParamSpec

from dataclasses import dataclass
from kine import Node, no_memo

from ...fullstack import IS_WEB_PLATFORM
from ...renderers.web_elements import a
from ... import Scope, component

from .router_impl import Map, Rule

if IS_WEB_PLATFORM or TYPE_CHECKING:
    import js

P = ParamSpec("P")

class UseRouter:
    def __init__(self, cx: Scope, routes: tuple[Route]):
        self.scope = cx
        self.map: Map[Node] = Map([Rule(route.route, route.child) for route in routes])

        location = js.document.location
        assert location

        self.current_route = location.pathname
        self.route_parameters: Mapping[str, Any] = {}

    def push_route(self, route: str):
        import pyodide.ffi

        self.current_route = route
        js.window.history.pushState(pyodide.ffi.to_js({}), "", route)

        self.scope.root_scope().schedule_update()

    def split_route(self, route: str) -> list[str]:
        return route.removeprefix("/").removeprefix("/").split("/")

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

@dataclass
class Route:
    route: str
    child: Node

@no_memo
@component
def router(cx: Scope, *routes: Route, not_found: Node | None = "404: Not Found"):
    router = cx.use_hook(lambda: cx.provide_context(UseRouter(cx, routes)))

    location = js.document.location
    assert location

    router.current_route = location.pathname

    match = router.map.match(location.pathname)

    if match:
        rule, dynamic_parts = match
        router.route_parameters = dynamic_parts

        return cx.render(rule.data)

    else:
        router.route_parameters = {}

        return cx.render(not_found)