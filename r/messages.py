from __future__ import annotations

from dataclasses import dataclass
from typing import (TYPE_CHECKING, Any, Generic, Literal, TypeVar, Union,
                    get_args)

if TYPE_CHECKING:
    from .utils import ElementId, ScopeId

T = TypeVar("T")

class BaseEvent(Generic[T]):
    type: T
    table: dict[str, Any] = {}
    __orig_bases__: tuple[type, ...]

    subclasses = Union["EventMessage", "Immediate", "DirtyAll", "NewTask"]

    def __init_subclass__(cls) -> None:
        cls.type = get_args(get_args(cls.__orig_bases__[0])[0])[0]
        cls.table[cls.type] = cls

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BaseEvent.subclasses:
        message_type: str = data.pop("type")

        return cls.table[message_type](**data)

@dataclass
class EventMessage(BaseEvent[Literal["asd"]]):
    scope_id: ScopeId | None
    priority: int
    element_id: ElementId | None
    name: str
    bubbles: bool
    data: Any

@dataclass
class Immediate(BaseEvent[Literal["Immediate"]]):
    scope_id: ScopeId

@dataclass
class DirtyAll(BaseEvent[Literal["DirtyAll"]]):
    pass

@dataclass
class NewTask(BaseEvent[Literal["NewTask"]]):
    scope_id: ScopeId


from_dict = BaseEvent.from_dict
ScheduleMessage = BaseEvent.subclasses
