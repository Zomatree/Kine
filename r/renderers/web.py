from typing import ParamSpec

from r.scope import Scopes
from ..r import Component, Node

P = ParamSpec("P")

async def start(app: Component[P], *args: P.args, **kwargs: P.kwargs):
    scopes = Scopes()

    cx = scopes.new_scope(None)
    inital_tree = app(cx, *args, **kwargs)

    diff = Diff(inital_tree)
