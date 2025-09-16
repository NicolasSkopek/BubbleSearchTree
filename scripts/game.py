import pygame

from scripts.obj import Obj
from scripts.scene import Scene

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()
        self.bg = Obj("assets/bg.png", [0,0],self.all_sprites)

        self.pts = 0
        self.hp = 3