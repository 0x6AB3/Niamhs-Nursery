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

    # Takes another GameObject and checks for a collision on the left or right
    def x_collision(self, other):
        sxl, sxr = self.x - self.width / 2, self.x + self.width / 2
        oxl, oxr = other.x - other.width / 2, other.x + other.width / 2

        collision_right = oxl <= sxr and oxl >= sxl
        collision_left = oxr >= sxl and oxr <= sxr

        if collision_left or collision_right:
            return True
        else:
            return False

    # 'syu' means: self, y-axis, up (top of GameObject)
    # 'd' for down, 'o' for other, etc
    def y_collision(self, other):
        syu, syd = self.y - self.height / 2, self.y + self.height / 2
        oyu, oyd = other.y - other.height / 2, other.y + other.height / 2

        #collision_up =
        #collision_down = oxr >= sxl and oxr <= sxr

        #if collision_up or collision_down:
        #    return True
        #else:
        #    return False