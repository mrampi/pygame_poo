from modulos.characters.Heroe import Heroe
from modulos.values.colores import PURPURA
from modulos.config import Config
import pygame as py

class Game(Config):

    def __init__(self, size, FPS, caption="Title", icon=""):
        super().__init__(size, FPS, caption, icon)

        self.set_heroe()

        self.pressed_keys = []
        
    def set_heroe(self):
        x = self.size[0] // 2
        y = self.size[1] - 160
        self.heroe = Heroe((50, 75), (x, y), 10)

    def move_heroe(self):
        if self.pressed_keys[py.K_RIGHT]:
            # print('right')
            self.heroe.move_right(self.size[0])
        elif self.pressed_keys[py.K_LEFT]:
            self.heroe.move_left(10)
        elif self.pressed_keys[py.K_UP]:
            self.heroe.move_up()
        elif self.pressed_keys[py.K_DOWN]:
            self.heroe.move_down()
        else:
            self.heroe.stop()

    def blit_heroe(self):
        self.screen.blit(self.heroe.image, self.heroe.rect)
        
    def init(self):
        py.init()

        while self.running:
            self.fill_screen(PURPURA)
            
            self.clock.tick(self.FPS)
            

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

            self.get_pressed()

            self.move_heroe()

            self.blit_heroe()

            py.display.flip()
        
        py.quit()

    def get_pressed(self):
        self.pressed_keys = py.key.get_pressed()