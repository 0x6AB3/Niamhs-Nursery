from Moveable import Moveable

class Niamh(Moveable):
    def __init__(self, controller, color=(255, 64, 64), width=50, height=100):
        super().__init__(
            controller,
            color,
            width,
            height,
            controller.width / 10,
            controller.height - height,
            500)

    def parent_collision_check(self):
        parent = self.controller.parent_spawner.parent
        if parent is not None:
            nx = self.x
            nxl, nxr = nx - self.width / 2, nx + self.width / 2
            px = parent.x
            pxl, pxr = px - parent.width / 2, px + parent.width / 2
            collision_right = pxl <= nxr and pxl >= nxl
            collision_left = pxr >= nxl and pxr <= nxr
            if collision_left or collision_right:
                print("collision detected")
