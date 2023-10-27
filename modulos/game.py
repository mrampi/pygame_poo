from modulos.characters.FallingObject import FallingObject
from modulos.characters.Heroe import Heroe
from modulos.values.assets import BACKGROUND_IMAGE, MARIO_MUSIC
from modulos.values.colores import BLANCO, PURPURA
from modulos.config import Config
import pygame as py

class Game(Config):

    def __init__(self, size, FPS, caption="Title", icon=""):
        super().__init__(size, FPS, caption, icon)

        self.set_background_image(BACKGROUND_IMAGE)

        self.set_heroe()
        self.set_falling_objects(28)        

        self.pressed_keys = []

        self.set_music(MARIO_MUSIC)
        
    def set_falling_objects(self, size):
        self.falling_objects = FallingObject.create_list(size, self.size)

    def set_heroe(self):
        x = self.size[0] // 2
        y = self.size[1] - 260

        self.heroe = Heroe((75, 100), (x, y), 10)
        
    def move_heroe(self):
        if self.pressed_keys[py.K_RIGHT]:
            self.heroe.move_right(self.size[0])
        elif self.pressed_keys[py.K_LEFT]:
            self.heroe.move_left(10)
        # elif self.pressed_keys[py.K_UP]:
        #     self.heroe.move_up()
        # elif self.pressed_keys[py.K_DOWN]:
        #     self.heroe.move_down()
        else:
            self.heroe.stop()

    def blit_heroe(self):
        self.heroe.blit(self.screen)
        # py.draw.rect(self.screen, BLANCO, self.heroe.rect, 3)
        # py.draw.rect(self.screen, BLANCO, self.heroe.mouth.rect, 3)

    def blit_falling_objects(self):
        for fo in self.falling_objects:
            fo.move_down()
            fo.blit(self.screen)

    def check_collides(self):
        self.heroe.collide_with_falling_objects(self.falling_objects)

        self.show_score(self.heroe.points)

    def init(self):
        py.init()

        while self.running:
            self.fill_screen()
            
            self.clock.tick(self.FPS)            

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

            self.get_pressed()

            self.move_heroe()

            self.blit_heroe()


            self.blit_falling_objects()

            self.check_collides()
            
            py.display.flip()
        
        py.quit()

    def get_pressed(self):
        self.pressed_keys = py.key.get_pressed()

    def show_score(self, text):
        # TODO: Hacer reutilizable
        font = py.font.SysFont('Arial', 30)
        text = font.render(f"Score: {text}", True, BLANCO)
        self.screen.blit(text, (0, 0))