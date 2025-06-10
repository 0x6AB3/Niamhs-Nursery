import time
import pygame
import threading

class Niamh:
    def __init__(self, controller):
        self.controller = controller

        self.color = (255, 128, 128)

        self.width = 50
        self.height = 100

        self.x = controller.width / 10
        self.target_x = self.x

        self.y =  controller.height - self.height

        self.speed = 500

    def set_target(self, x):
        self.target_x = x - self.width / 2

    def update(self, dt):
        difference = self.target_x - self.x
        if abs(difference) > 1:
            direction = 1 if difference > 0 else -1
            self.x += direction * self.speed * dt
        else:
            self.x = self.target_x

    def draw(self):
        pygame.draw.rect(self.controller.screen, self.color, (self.x, self.y, self.width, self.height))
