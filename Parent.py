from Moveable import Moveable
from ParentBubble import ParentBubble

class Parent(Moveable):
    def __init__(self, controller, color=(0, 255, 0), width=50, height=80):
        super().__init__(
            controller,
            color,
            width,
            height,
            int(controller.width * 1.1),
            controller.height - height,
            250,
            int(controller.width * 0.75)
        )
        self.show_bubble = False
        self.bubble = None

    def update(self, dt):
        super().update(dt)

        self.show_bubble = True if self.controller.niamh.x_collision(self) else False

        if self.show_bubble:
            x = self.x - self.width / 2
            y = self.y - self.height * 1.5
            self.bubble = ParentBubble(self.controller, x, y)
        else:
            self.bubble = None

    def draw(self):
        super().draw()
        if self.show_bubble and self.bubble is not None:
            self.bubble.draw()