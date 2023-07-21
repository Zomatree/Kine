from ... import component, Scope
from ...renderers.web_elements import *
from typing import ParamSpec, overload, TypeVar
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


T = TypeVar("T")


class Storage:
    def __init__(self, cx: Scope, backing: js.Storage):
        self.cx = cx
        self.backing = backing

    @overload
    def get(self, name: str, default: T) -> str | T:
        ...

    @overload
    def get(self, name: str, default: None = ...) -> str | None:
        ...

    def get(self, name: str, default: T | None = None) -> str | None | T:
        return self.backing.getItem(name) or default

    def set(self, name: str, value: str):
        self.backing.setItem(name, value)
        self.cx.schedule_update()

    def remove(self, name: str):
        self.backing.removeItem(name)
        self.cx.schedule_update()

    def clear(self):
        self.backing.clear()
        self.cx.schedule_update()

    @overload
    def key(self, index: int, default: T) -> str | T:
        ...

    @overload
    def key(self, index: int, default: None = ...) -> str | None:
        ...

    def key(self, index: int, default: T | None = None) -> str | None | T:
        return self.backing.key(index) or default

    def __len__(self) -> int:
        return self.backing.length

    def __getitem__(self, key: str) -> str:
        value = self.get(key)

        if value is None:
            raise IndexError

        return value

    def __setitem__(self, key: str, value: str):
        self.set(key, value)


def use_local_storage(cx: Scope) -> Storage:
    return cx.use_hook(lambda: Storage(cx, js.window.localStorage))


def use_session_storage(cx: Scope) -> Storage:
    return cx.use_hook(lambda: Storage(cx, js.window.sessionStorage))
