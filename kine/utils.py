import asyncio
from asyncio import Future
from dataclasses import dataclass
from typing import NewType, TypeVar

T = TypeVar("T")

ScopeId = NewType("ScopeId", int)
TaskId = NewType("TaskId", tuple[int, ScopeId])
ElementId = NewType("ElementId", int)


async def select(*futures: Future[T]) -> tuple[int, T]:
    new_futures: list[Future[tuple[int, T]]] = []

    for i, fut in enumerate(futures):

        async def wrapper(i: int, fut: Future[T]):
            return i, await fut

        new_futures.append(asyncio.ensure_future(wrapper(i, fut)))

    (task,), _ = await asyncio.wait(new_futures, return_when=asyncio.FIRST_COMPLETED)

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
