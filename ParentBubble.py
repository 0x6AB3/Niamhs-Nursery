from GameObject import GameObject

class ParentBubble(GameObject):
    def __init__(self, controller, x, y):
        super().__init__(
            controller,
            (255, 255, 255),
            100,
            100,
            x,
            y
        )

    def on_click(self):
        pass