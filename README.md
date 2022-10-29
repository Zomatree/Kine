# R

*(temporary name until i find an actual name)*


A react style gui framework in python.



### Example

```py
import asyncio
from r import *

@component
def app(cx: Scope):
    value = use_state(cx, lambda: 0)

    return cx.render(div()[
        button(
            onclick=lambda _: value.modify(lambda v: v - 1)
        )[
            "Minus"
        ],
        str(value.get()),
        button(
            onclick=lambda _: value.modify(lambda v: v + 1)
        )[
            "Add"
        ],
    ])

asyncio.run(web.start(app()))
```
