# Kine

![Logo and name](.github/logo_name.png)

Kine is a web-based gui framework with support for reactive code and ease of use.

Supports both liveview-style server-side rendering and running client side via WASM.


### Example

See a version of this example running live [here](https://zomatree.github.io/kine)

```py
import asyncio

from kine import *
from kine.renderers.web import *

@component
def app(cx: Scope):
    value = use_state(cx, lambda: 0)

    return div[
        button(
            onclick=lambda _: value.modify(lambda v: v + 1)
        )[
            "+1"
        ],
        f"{value.get()}",
        button(
            onclick=lambda _: value.modify(lambda v: v - 1)
        )[
            "-1"
        ],
    ]

asyncio.run(start_web(app()))
```
