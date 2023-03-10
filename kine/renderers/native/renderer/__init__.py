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

    messages = Column()
    input = Input()
    button = Button()
    button.add_child(Label("Enter"))

    row = Row()
    row.add_child(input)
    row.add_child(button)

    def on_click():
        label = Label(input.text)
        input.text = ""

        messages.add_child(label)

    window.add_child(messages)
    window.add_child(row)

    window.root.print_tree()
    window.run()
