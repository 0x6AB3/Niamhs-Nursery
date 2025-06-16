import pygame

from Niamh import Niamh
from BabyBed import BabyBed
from ParentSpawner import ParentSpawner

class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Niamh's Nursery")
        programIcon = pygame.image.load('icon.jpg')
        pygame.display.set_icon(programIcon)
        self.font = pygame.font.SysFont(None, 72)
        self.width = 1200
        self.height = 600
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()

        self.money = 0

        # Game components
        self.background_image = pygame.image.load("NurseryBackground.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height*1.2))
        self.niamh = Niamh(self)
        self.parent_spawner = ParentSpawner(self)
        self.bed = BabyBed(self)

    def update_money(self):
        money_text = self.font.render(f"£{self.money}", True, (255, 255, 0))
        self.screen.blit(money_text, (0, 0))

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
            self.screen.blit(self.background_image, (0, 0))

            # Update objects
            self.niamh.update(dt)
            self.parent_spawner.update(dt)

            # Draw objects
            self.bed.draw()
            self.parent_spawner.draw()
            self.niamh.draw()
            self.update_money()

            # Update display
            pygame.display.update()

if __name__ == "__main__":
    controller = Controller()
    controller.run()