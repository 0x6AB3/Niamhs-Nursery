import pygame

class GameObject:
    def __init__(self, controller, color=(255, 255, 255), width=50, height=50, x=0, y=0):
        self.controller = controller
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.controller.screen, self.color, (self.x, self.y, self.width, self.height))
