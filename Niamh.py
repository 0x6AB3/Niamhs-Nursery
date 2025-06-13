from Moveable import Moveable

class Niamh(Moveable):
    def __init__(self, controller, color=(255, 64, 64), width=50, height=100):
        super().__init__(
            controller,
            color,
            width,
            height,
            controller.width / 10,
            controller.height - height,
            500
        )
        self.carrying_baby = False
        self.carrying_baby_count = 0

    def add_baby(self, count):
        self.carrying_baby += count