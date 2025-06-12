import pygame

from Parent import Parent

class ParentSpawner:
    def __init__(self, controller):
        self.interval = 60 # seconds
        self.parent = Parent(controller) # spawn parent immediately
        self.spawned_time = pygame.time.get_ticks()
        self.controller = controller

    def update(self, dt):
        # Spawn parent if enough time passed and one doesn't exist
        if self.parent is None and self.difference(self.spawned_time, pygame.time.get_ticks()) >= self.interval:
            self.parent = Parent(self.controller)
            self.spawned_time = pygame.time.get_ticks()

        # Update parent
        if self.parent is not None:
            self.parent.update(dt)

    def draw(self):
        if self.parent is not None:
            self.parent.draw()

    def difference(self, start, end):
        return (end - start) / 1000 # seconds