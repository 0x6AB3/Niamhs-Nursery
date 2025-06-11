from Moveable import Moveable

class Parent(Moveable):
    def __init__(self, controller, color=(0, 255, 0), width=50, height=80):
        super().__init__(
            controller,
            color,
            width,
            height,
            int(controller.width * 1.1),
            controller.height - height,
            250,
            int(controller.width * 0.75)
        )
