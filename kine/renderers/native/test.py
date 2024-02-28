from kine.renderers.native import *


class MyWindow(Window):
    def __init__(self, width: int, height: int):
        self.i = 0

        super().__init__("Test", width, height)

    def decr(self, event: MouseEvent):
        self.i -= 1

    def incr(self, event: MouseEvent):
        self.i += 1

    def nodes(self):
        return Node(
            layout=Layout(size=(self.width, self.height), align_items=AlignItems.CENTER, justify_content=JustifyContent.CENTER, gap=16),
            style=Style(font_size=16, foreground=BLACK)
        ).add(
            Node(
                layout=Layout(padding=8),
                style=Style(background=BLACK, foreground=WHITE),
                events={
                    "click": [self.decr]
                }
            ).add(
                TextNode("-1")
            ),
            TextNode(str(self.i)),
            Node(
                layout=Layout(padding=8),
                style=Style(background=BLACK, foreground=WHITE),
                events={
                    "click": [self.incr]
                }
            ).add(
                TextNode("+1")
            )
        )


if __name__ == "__main__":
    window = MyWindow(800, 600)
    window.run()