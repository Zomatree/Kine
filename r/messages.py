from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypeAlias, get_args

if TYPE_CHECKING:
    from .utils import ElementId, ScopeId

@dataclass
class EventMessage:
    type = "EventMessage"

    scope_id: ScopeId | None
    priority: int
    element_id: ElementId | None
    name: str
    bubbles: bool
    data: Any

@dataclass
class Immediate:
    type = "Immediate"
    scope_id: ScopeId

@dataclass
class DirtyAll:
    type = "DirtyAll"

@dataclass
class NewTask:
    type = "NewTask"
    scope_id: ScopeId

ScheduleMessage: TypeAlias = EventMessage | Immediate | DirtyAll | NewTask

lookup_table = { cls.type: cls for cls in get_args(ScheduleMessage) }

def from_dict(data: dict[str, Any]) -> ScheduleMessage:
    message_type: str = data.pop("type")

    return lookup_table[message_type](**data)
