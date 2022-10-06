from __future__ import annotations
from collections import deque
from dataclasses import dataclass
import asyncio

from typing import TYPE_CHECKING, Any, TypeAlias, TypeVar, cast

from r.scope import ElementId, ScopeId, Scopes

if TYPE_CHECKING:
    from .core import Component

T = TypeVar("T")

@dataclass
class EventMessage:
    scope_id: ScopeId | None
    priority: int
    element_id: ElementId | None
    name: str
    bubbles: bool
    data: Any

@dataclass
class Immediate:
    scope_id: ScopeId

@dataclass
class DirtyAll:
    pass

@dataclass
class NewTask:
    scope_id: ScopeId

ScheduleMessage: TypeAlias = EventMessage | Immediate | DirtyAll | NewTask

class VirtualDom:
    def __init__(self, scopes: Scopes):
        self.scopes = scopes
        self.dirty_scopes = {ScopeId(0)}
        self.messages: asyncio.Queue[ScheduleMessage] = asyncio.Queue()
        self.pending_messages = deque[ScheduleMessage]()

    async def _task(self):
        while True:
            for task_id, task in list(self.scopes.tasks.tasks.items()):
                if not task.done():
                    del self.scopes.tasks.tasks[task_id]

            if self.scopes.tasks.tasks:
                return
            else:
                await asyncio.sleep(0)

    async def wait_for_work(self):
        while True:
            if self.dirty_scopes and not self.messages:
                break

            if self.messages.empty():
                if self.scopes.tasks.tasks:
                    loop_task = asyncio.create_task(self._task())
                    message_task = asyncio.create_task(self.messages.get())

                    done, _ = await asyncio.wait((loop_task, message_task), return_when=asyncio.FIRST_COMPLETED)

                    if message_task in done:
                        msg, = cast(set[asyncio.Task[EventMessage]], done)
                        self.pending_messages.appendleft(msg.result())
                else:
                    self.pending_messages.appendleft(await self.messages.get())

            self.process_all_messages()

    def process_all_messages(self):
        try:
            while True:
                self.pending_messages.appendleft(self.messages.get_nowait())
        except asyncio.QueueEmpty:
            pass

        try:
            while True:
                message = self.pending_messages.pop()
                self.process_message(message)
        except IndexError:
            pass

    def process_message(self, message: ScheduleMessage):
        match message:
            case NewTask():
                pass  # dont need to do anything

            case EventMessage() as event:
                self.scopes.call_listener_with_bubbling(event)

            case Immediate(scope_id):
                self.dirty_scopes.add(scope_id)

            case DirtyAll():
                for id in self.scopes.scopes:
                    self.dirty_scopes.add(id)
