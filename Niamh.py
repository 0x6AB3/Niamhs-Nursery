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
        self.carrying_baby_limit = 1

    def add_baby(self):
        if self.carrying_baby_count != self.carrying_baby_limit:
            self.carrying_baby_count += 1
            return True
        return False