import asyncio
from asyncio import Task
from dataclasses import dataclass
from typing import Awaitable, NewType, TypeVar

T = TypeVar("T")
U = TypeVar("U")

ScopeId = NewType("ScopeId", int)
TaskId = NewType("TaskId", tuple[int, ScopeId])
ElementId = NewType("ElementId", int)


async def select(*futures: tuple[T, Awaitable[U]]) -> tuple[T, U]:
    new_futures: list[Task[tuple[T, U]]] = []

    for v, fut in futures:

        async def wrapper(i: T, fut: Awaitable[U]):
            return v, await fut

        new_futures.append(asyncio.create_task(wrapper(v, fut)))

    (task,), pending = await asyncio.wait(new_futures, return_when=asyncio.FIRST_COMPLETED)

    for t in pending:
        t.cancel()

    return task.result()


@dataclass
class Lis:
    output: list[int]
    predecessors: list[int]
    starts: list[int]


def find_lis(items: list[int]) -> Lis:
    length = len(items)
    lis = Lis([], [0 for _ in range(length)], [0 for _ in range(length)])

    if not items:
        return lis

    k = 0

    for i, item in enumerate(items):
        j = lis.starts[k]

        if items[j] < item:
            lis.predecessors[i] = j
            k += 1
            lis.starts[k] = i
            continue

        lo = 0
        hi = k

        while lo < hi:
            mid = (lo >> 1) + (hi >> 1) + (lo & hi & 1)

            if items[lis.starts[mid]] < items[i]:
                lo = mid + 1
            else:
                hi = mid

        if items[i] < items[lis.starts[lo]]:
            if lo > 0:
                lis.predecessors[i] = lis.starts[lo - 1]

            lis.starts[lo] = i

    u = k + 1
    v = lis.starts[k]

    for _ in reversed(range(u)):
        w = v
        v = lis.predecessors[v]
        lis.output.append(w)

    return lis
