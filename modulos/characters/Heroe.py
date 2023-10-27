import pygame as py

from modulos.characters.FallingObject import FallingObject
from modulos.characters.object import Object
from modulos.values.assets import MARIO_COIN_SOUND, MARIO_IMAGE, MARIO_MUSIC


class Heroe(Object):

    def __init__(self, size, position=(0,0), speed=5) -> None:
        self.mouth = Object((20, 10), (0, 0))
        
        
        super().__init__(size, position, MARIO_IMAGE)
        
        self.image_left = py.transform.flip(self.image, True, False)
        self.image_right = self.image
        

        self.points = 0

        # self.mouth.set_speed(speed)
        self.set_speed(speed)

        self.mouth.rect.center = self.rect.center

        # self.mouth.image.fill((255, 0, 0))

    def set_speed(self, speed):
        self.speed = speed
        self.mouth.set_speed(speed)

    def move_right(self, top_right):
        new_x = self.rect.x + self.speed

        if new_x >= 0 and new_x <= top_right - self.rect.width:
            self.image = self.image_right
            self.mouth.move_right()
            super().move_right()

    def move_left(self, top_left):
        new_x = self.rect.x - self.speed

        if new_x >= top_left:
            self.image = self.image_left
            self.mouth.move_left()
            super().move_left()

    def collide_with_falling_objects(self, falling_objects:list['FallingObject']):
        for fo in falling_objects:
            # if self.rect.colliderect(fo.rect):
            if self.mouth.rect.colliderect(fo.rect):
                fo.set_random_position()
                self.collide_fo_effects()
                self.points += 1
            
    def collide_fo_effects(self):
        # TODO: Refactorizar
        #  FIXME: Refactorizar
        music = py.mixer.Sound(MARIO_COIN_SOUND)
        music.set_volume(0.5)
        music.play()

    def blit(self, screen):
        screen.blit(self.mouth.image, self.mouth.rect)
        super().blit(screen)

        