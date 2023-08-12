from __future__ import annotations

from typing import Any, Mapping, TypeVar, Generic

T = TypeVar("T")

class Rule(Generic[T]):
    def __init__(self, route: str, data: T):
        self.route = route
        self.data = data

        self.parts = list(map(RoutePart, filter(None, route.split("/"))))

    def __repr__(self) -> str:
        return f"<Rule route={self.route!r} parts={self.parts!r}>"

class RoutePart:
    def __init__(self, raw_part: str):
        self.raw_part = raw_part
        self.name: str = raw_part
        self.dynamic: bool = False

        if raw_part.startswith("<") and raw_part.endswith(">"):
            self.name = raw_part[1:-1]
            self.dynamic = True

    def __repr__(self) -> str:
        return f"<RoutePart name={self.name!r} dynamic={self.dynamic!r}>"

class Map(Generic[T]):
    def __init__(self, rules: list[Rule[T]] | None = None):
        self.rules: list[Rule[T]] = rules or []

    def add_rule(self, rule: Rule[T]):
        self.rules.append(rule)

    def match(self, path: str) -> tuple[Rule[T], Mapping[str, Any]] | None:
        parts = list(filter(None, path.split("/")))

        matching_rules: list[tuple[Rule[T], dict[str, str]]] = [(rule, {}) for rule in self.rules]

        for i, part in enumerate(parts):
            currently_matching_rules: list[tuple[Rule[T], dict[str, str]]] = []

            for rule, dynamic_parts in matching_rules:
                if i < len(rule.parts):
                    route_part = rule.parts[i]

                    matches = route_part.dynamic

                    if matches:
                        dynamic_parts[route_part.name] = part
                    else:
                        if route_part.name == part:
                            matches = True

                    if matches:
                        currently_matching_rules.append((rule, dynamic_parts))

            matching_rules = currently_matching_rules

        matching_rules = [(rule, dyn_parts) for (rule, dyn_parts) in matching_rules if len(rule.parts) == len(parts)]

        if matching_rules:
            return matching_rules[0]

    def __repr__(self) -> str:
        return f"<Map rules={self.rules!r}>"
