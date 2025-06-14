import pygame

from GameObject import GameObject

class BabyBed(GameObject):
    def __init__(self, controller, color=(128, 32, 32), width=100, height=150, x=0, y=0, baby_limit = 1):
        super().__init__(
            controller,
            color,
            width,
            height,
            int(controller.width * 0.1),
            controller.height - height
        )
        self.babies = []
        self.capacity = baby_limit

    def draw(self):
        super().draw()
        collision = self.controller.niamh.x_collision(self)
        carrying = len(self.controller.niamh.babies) > 0
        bed_space = len(self.babies) < self.capacity
        niamh_space = len(self.controller.niamh.babies) < self.controller.niamh.capacity

        if collision and carrying and bed_space:
            baby = self.controller.niamh.remove_baby()
            if baby is None:
                return
            baby.put_to_sleep(self)

        if collision and not carrying and not bed_space and not self.babies[0].tired() and niamh_space:
            if self.babies[0].awake(self.controller.niamh):
                del self.babies[0]

        if len(self.babies) > 0:
            self.color = (255, 255, 255)

        if len(self.babies) == 0:
            self.color = (128, 32, 32)
