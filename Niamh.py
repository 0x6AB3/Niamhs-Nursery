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
        for i in range(2):
            img = pygame.image.load(f"NiamhIdle{i+1}.png").convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            self.idle_images.append(scaled_img)

        self.idle_index = 0
        self.idle_start = pygame.time.get_ticks()
        self.animation_rect = pygame.Rect(self.x - self.width / 2, self.y - 20, self.width, self.height)
        self.animation_image = self.idle_images[self.idle_index]

    def draw(self):
        #super().draw()
        self.draw_animation()

    def update(self, dt):
        super().update(dt)
        if self.x == self.target_x:
            self.update_idle()
            self.animation_rect.x = 10 + self.x - self.width

    def update_idle(self):
        if pygame.time.get_ticks() - self.idle_start > 250:
            self.idle_index += 1 if not self.idle_index == len(self.idle_images)-1 else -self.idle_index
            self.idle_start = pygame.time.get_ticks()
            self.animation_image = self.idle_images[self.idle_index]

    def draw_animation(self):
        self.controller.screen.blit(self.animation_image, self.animation_rect)

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