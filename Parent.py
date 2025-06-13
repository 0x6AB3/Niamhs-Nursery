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
        self.bubble = None
        self.leaving = False
        self.finished = False

    def update(self, dt):
        super().update(dt)

        if self.x == self.target_x and self.leaving:
            self.finished = True

        if self.x == self.target_x:
            x = self.x - self.width / 2
            y = self.y - self.height * 1.5
            self.bubble = ParentBubble(self.controller, x, y)

        if self.controller.niamh.x_collision(self) and self.bubble is not None:
            self.bubble = None
            self.leaving = True
            self.target_x = int(self.controller.width * 1.1)
            self.controller.niamh.add_baby(1)


    def draw(self):
        super().draw()
        if self.bubble is not None:
            self.bubble.draw()