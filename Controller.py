import pygame
from Niamh import Niamh

class Controller:
    def __init__(self):
        self.width = 1200
        self.height = 600
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Niamh's Nursery'")
        self.niamh = Niamh(self)

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(240) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_x = pygame.mouse.get_pos()[0]
                    self.niamh.set_target(new_x)

            self.screen.fill((32,16,128))
            self.niamh.update(dt)
            self.niamh.draw()
            pygame.display.update()

if __name__ == "__main__":
    controller = Controller()
    controller.run()