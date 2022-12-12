from r import *
from r.renderers.wasm import *
from r.renderers.wasm.utils import get

@component
def app(cx: Scope):
    config: UseState[dict[str, Any] | None] = use_state(cx, lambda: None)

    async def get_config():
        resp = await get("https://httpbin.org/get")
        config.set(await resp.json())

    use_future(cx, get_config)

    return cx.render(div[
        p[
            f"{config.get()}"
        ]
    ])
