from typing import ParamSpec

from r.core import ComponentFunction, VNode
from r.dom import VirtualDom
from r.utils import ScopeId

P = ParamSpec("P")

def transform_vnode(node: VNode) -> str:
    ...

async def start(app: ComponentFunction[P], *args: P.args, **kwargs: P.kwargs):

    dom = VirtualDom(app)
    mutations = dom.rebuild()

    dom.scopes.run_scope(ScopeId(0))
