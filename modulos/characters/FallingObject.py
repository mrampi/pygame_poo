from modulos.characters.object import Object
import random

class FallingObject(Object):
    def __init__(self, size_surface, position, screen) -> None:
        super().__init__(size_surface, position)

        self.screen = screen
        self.set_random_position()

        # self.set_speed()
        #  Otra forma
        speed = random.randrange(3, 7)
        self.set_speed(speed)

    def move_down(self):
        if self.rect.y > self.screen[1]:
            self.set_random_position()
        else:
            super().move_down()

    def set_random_position(self):        
        self.rect.x = random.randrange(self.rect.width, self.screen[0] - self.rect.width)
        self.rect.y = random.randrange(-100, -40)

    # def set_speed(self):
    #     speed = random.randrange(3, 7)

    #     super().set_speed(speed)
    
    @staticmethod
    def create_list(size, screen):
        list = []

        for i in range(size):
            falling_object = FallingObject((50, 50), (0,0), screen)
            list.append(falling_object)

        return list