from __future__ import annotations

import contextlib, glfw, skia
from OpenGL import GL
from typing import Any

@contextlib.contextmanager
def glfw_window(width: int, height: int, title: str):
    if not glfw.init():
        raise RuntimeError('glfw.init() failed')

    glfw.window_hint(glfw.STENCIL_BITS, 8)

    window = glfw.create_window(width, height, title, None, None)

    glfw.make_context_current(window)

    try:
        yield window
    finally:
        glfw.terminate()

@contextlib.contextmanager
def skia_surface(window: Any):
    context = skia.GrDirectContext.MakeGL()

    (fb_width, fb_height) = glfw.get_framebuffer_size(window)

    backend_render_target = skia.GrBackendRenderTarget(fb_width, fb_height, 0, 0, skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))

    surface = skia.Surface.MakeFromBackendRenderTarget(
        context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
        skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())

    try:
        yield surface
    finally:
        context.abandonContext()