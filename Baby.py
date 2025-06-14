import pygame

from GameObject import GameObject

class Baby(GameObject):
    def __init__(self, controller, color=(255, 255, 255), width=50, height=50, x=0, y=0, tired=True, sleep_required=10):
        super().__init__(
            controller,
            color,
            width,
            height,
            x,
            y
        )
        self.sleep_start = None
        self.sleep_required = sleep_required
        self.pick_up_sound = pygame.mixer.Sound("PickUpBaby.wav")
        self.sleep_sound = pygame.mixer.Sound("BabySleep.wav")

    def tired(self):
        if (pygame.time.get_ticks() - self.sleep_start) / 1000 >= self.sleep_required:
            return False
        return True

    def awake(self, niamh):
        if not self.tired:
            niamh.add_baby(self)
            return True
        return False

    def put_to_sleep(self, bed):
        if self.tired:
            bed.add_baby(self)
            self.sleep_start = pygame.time.get_ticks()
            self.sleep_sound.play()

