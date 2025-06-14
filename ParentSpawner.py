import pygame
from random import randint

from Parent import Parent

class ParentSpawner:
    def __init__(self, controller):
        self.interval = randint(3, 10) # seconds
        self.parent = Parent(controller) # spawn parent on game start
        self.spawned_time = pygame.time.get_ticks()
        self.controller = controller

    def update(self, dt):
        if self.parent is not None and self.parent.finished == True:
            self.parent = None
            self.interval = randint(3, 10)

        # Spawn parent if enough time passed and one doesn't exist
        elif self.parent is None and self.difference(self.spawned_time, pygame.time.get_ticks()) >= self.interval:
            self.parent = Parent(self.controller)
            self.spawned_time = pygame.time.get_ticks()

        # Update parent
        elif self.parent is not None:
            self.parent.update(dt)

    def draw(self):
        if self.parent is not None:
            self.parent.draw()

    def difference(self, start, end):
        return (end - start) / 1000 # seconds