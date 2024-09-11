from __future__ import annotations

from typing import TYPE_CHECKING

from .core import component

if TYPE_CHECKING:
    from .core import Scope, CallableComponent

__all__ = ("error_boundary",)

class _ErrorBoundary:
    def __init__(self, fallback: CallableComponent[Exception]):
        self.fallback = fallback
        
@component
def error_boundary(cx: Scope, *, fallback: CallableComponent[Exception]):
    if len(cx.children) != 1:
        raise Exception("error_boundary must have one child")
    
    component = cx.children[0]
    
    cx.provide_context(_ErrorBoundary(fallback))
    
    return component
