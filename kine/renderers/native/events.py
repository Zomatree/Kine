class BaseEvent:
    def __init__(self, bubbles: bool = True) -> None:
        self.bubbles: bool = bubbles

    def prevent_bubbling(self):
        self.bubbles = False

class MouseEvent(BaseEvent):
    def __init__(self, button: int, position: tuple[int, int]) -> None:
        super().__init__(bubbles=True)
        self.button: int = button
        self.position: tuple[int, int] = position
