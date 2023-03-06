from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from .widgets import BaseWidget


def recursive_find_at_pos(widgets: Iterable[BaseWidget], position: tuple[int, int]) -> list[BaseWidget]:
    found: list[BaseWidget] = []

    for widget in widgets:
        if widget.is_intersecting(position):
            found.append(widget)
            found.extend(recursive_find_at_pos(widget.children, position))

    return found
