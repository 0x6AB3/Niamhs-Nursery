from inspect import stack

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
        self.babies = []
        self.capacity = 1

    def add_baby(self, baby):
        if len(self.babies) < self.capacity:
            self.babies.append(baby)
            baby.pick_up_sound.play()
            return True
        return False

    def remove_baby(self):
        if len(self.babies) > 0:
            return self.babies.pop()
        return None