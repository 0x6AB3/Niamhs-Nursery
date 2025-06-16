import pygame

from Moveable import Moveable

class Niamh(Moveable):
    def __init__(self, controller, color=(255, 64, 64), width=50, height=100):
        super().__init__(
            controller,
            color,
            width,
            height,
            controller.width / 7,
            controller.height - height,
            500
        )
        self.babies = []
        self.capacity = 1

        self.idle_images = []
        self.run_images = []
        for i in range(2):
            img = pygame.image.load(f"NiamhIdle{i+1}.png").convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            self.idle_images.append(scaled_img)

        for i in range(2):
            img = pygame.image.load(f"NiamhRun{i+1}.png").convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            self.run_images.append(scaled_img)

        self.idle_index = 0
        self.idle_start = pygame.time.get_ticks()
        self.run_index = 0
        self.run_start = pygame.time.get_ticks()
        self.animation_rect = pygame.Rect(self.x - self.width / 2, self.y - 20, self.width, self.height)
        self.animation_image = self.idle_images[self.idle_index]
        self.facing_left = False

    def draw(self):
        #super().draw() # show collision box
        self.draw_animation()

    def update(self, dt):
        old_x = self.x
        super().update(dt)
        self.facing_left = True if old_x - self.x  > 0 else False
        self.animation_rect.x = 10 + self.x - self.width
        self.update_idle() if self.x == self.target_x else self.update_run()


    def update_run(self):
        if pygame.time.get_ticks() - self.run_start > 250:
            self.run_index += 1 if not self.run_index == len(self.run_images)-1 else -self.run_index
            self.run_start = pygame.time.get_ticks()
            self.animation_image = self.run_images[self.run_index]


    def update_idle(self):
        if pygame.time.get_ticks() - self.idle_start > 250:
            self.idle_index += 1 if not self.idle_index == len(self.idle_images)-1 else -self.idle_index
            self.idle_start = pygame.time.get_ticks()
            self.animation_image = self.idle_images[self.idle_index]

    def draw_animation(self):
        if self.facing_left:
            image = pygame.transform.flip(self.animation_image, True, False)
        else:
            image = self.animation_image
        self.controller.screen.blit(image, self.animation_rect)

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