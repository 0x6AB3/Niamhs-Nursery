import pygame

from Niamh import Niamh
from BabyBed import BabyBed
from ParentSpawner import ParentSpawner

class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Niamh's Nursery'")
        self.width = 1200
        self.height = 600
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()

        # Game components
        self.niamh = Niamh(self)
        self.parent_spawner = ParentSpawner(self)
        self.bed = BabyBed(self)

    def run(self):
        running = True
        while running:
            # Time since last frame (240Hz)
            dt = self.clock.tick(240) / 1000

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_x = pygame.mouse.get_pos()[0]
                    self.niamh.set_target(new_x)

            # Background
            self.screen.fill((0,128,255))

            # Update objects
            self.niamh.update(dt)
            self.parent_spawner.update(dt)

            # Draw objects
            self.bed.draw()
            self.parent_spawner.draw()
            self.niamh.draw()

            # Update display
            pygame.display.update()

if __name__ == "__main__":
    controller = Controller()
    controller.run()