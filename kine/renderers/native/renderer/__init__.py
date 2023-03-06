from __future__ import annotations

import pyglet

from .window import Window
from .widgets import *

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)


def main():
    window = Window()
    window.root.padding = 5

    window.add_child(Input())

    window.root.print_tree()
    window.run()
