from typing import TypeVar

T = TypeVar("T")

def create_proxy(f: T) -> T: ...
def to_js(v: T) -> T: ...
