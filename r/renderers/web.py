from typing import ParamSpec
from ..r import Component

P = ParamSpec("P")

async def start(app: Component[P], *args: P.args, **kwargs: P.kwargs):
    ...
