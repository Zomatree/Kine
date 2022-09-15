from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..r import Component

class VirtualDom:
    def __init__(self, app: Component):
        self.app = app
        self.dirty_scopes = [0]
        self.messages = []

    async def wait_for_work(self):
        while True:
            if self.dirty_scopes and not self.messages:
                break

            if not self.messages:
                ...
