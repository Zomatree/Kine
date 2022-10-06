from typing import ParamSpec

from r.core import VNode


from .. import Scopes, Component, transform_node, set_ids

P = ParamSpec("P")

def transform_vnode(node: VNode) -> str:
    ...

async def start(app: Component[P], *args: P.args, **kwargs: P.kwargs):
    scopes = Scopes()

    scope_id = scopes.new_scope(None)
    cx = scopes.get_scope(scope_id)

    inital_tree = app(cx, *args, **kwargs)

    set_ids(scopes, inital_tree)

    vnode = transform_node(scopes, inital_tree)

    while True:
