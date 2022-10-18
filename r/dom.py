from __future__ import annotations

import asyncio
from collections import deque
from typing import Callable, TypeVar, cast

from r.core import ComponentFunction

from .diff import AppendChildren, Diff, Mutations
from .messages import (DirtyAll, EventMessage, Immediate, NewTask,
                       ScheduleMessage)
from .scope import Scopes
from .utils import ElementId, ScopeId

T = TypeVar("T")


class VirtualDom:
    def __init__(self, app: ComponentFunction[...]):
        self.scopes = Scopes(app)
        self.scopes.dom = self

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

    def handle_message(self, message: ScheduleMessage):
        self.messages.put_nowait(message)
        self.process_all_messages()

    def rebuild(self):
        scope_id = ScopeId(0)

        diff_state = Diff(self.scopes)
        self.scopes.run_scope(scope_id)

        diff_state.element_stack.append(ElementId(0))
        diff_state.scope_stack.append(scope_id)

        node = self.scopes.get_scope(scope_id).fin_frame()
        created = diff_state.create_node(node)

        diff_state.mutations.append(AppendChildren(created))

        return diff_state.mutations

    def work_with_deadline(self, deadline: Callable[[], bool]) -> list[Mutations]:
        mutations: list[Mutations] = []

        while self.dirty_scopes:
            diff = Diff(self.scopes)
            ran_scopes: set[ScopeId] = set()

            self.dirty_scopes = {scope_id for scope_id in self.dirty_scopes if scope_id in self.scopes.scopes}

            self.dirty_scopes = set(sorted(self.dirty_scopes, reverse=True))

            if self.dirty_scopes:
                scope_id = self.dirty_scopes.pop()

                if scope_id not in ran_scopes:
                    ran_scopes.add(scope_id)

                    self.scopes.run_scope(scope_id)
                    diff.diff_scope(scope_id)

                    for dirty_scope_id in diff.mutations.dirty_scopes:
                        try:
                            self.dirty_scopes.remove(dirty_scope_id)
                        except KeyError:
                            pass

                    if diff.mutations.modifications:
                        mutations.append(diff.mutations)

                    # todo: more stuff

        return mutations
