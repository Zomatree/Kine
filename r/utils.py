import asyncio
from asyncio import Future
from typing import NewType, TypeVar

T = TypeVar("T")

ScopeId = NewType("ScopeId", int)
TaskId = NewType("TaskId", tuple[int, ScopeId])
ElementId = NewType("ElementId", int)

async def select(*futures: Future[T]) -> tuple[int, T]:
    new_futures: list[Future[tuple[int, T]]] = []

    for i, fut in enumerate(futures):
        async def wrapper(i: int = i):
            return i, await fut

        new_futures.append(asyncio.ensure_future(wrapper()))

    (task,), _ = await asyncio.wait(new_futures, return_when=asyncio.FIRST_COMPLETED)

    return task.result()
