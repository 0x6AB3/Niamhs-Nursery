from GameObject import GameObject

class Moveable(GameObject):
    def __init__(self, controller, color=(255, 255, 255), width=50, height=50, x=0, y=0, speed=250, target_x=None):
        super().__init__(
            controller,
            color,
            width,
            height,
            x,
            y
        )
        self.speed = speed
        self.target_x = target_x if target_x is not None else x

    def set_target(self, x):
        self.target_x = x - self.width / 2

    def update(self, dt):
        difference = self.target_x - self.x
        if abs(difference) > 1:
            direction = 1 if difference > 0 else -1
            self.x += direction * self.speed * dt
        else:
            self.x = self.target_x