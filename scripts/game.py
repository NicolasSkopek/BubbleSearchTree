import pygame

from scripts.obj import Obj, Knot
from scripts.scene import Scene

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()
        self.bg = Obj("assets/bg.png", [0,0],self.all_sprites)
        self.generate_tree()

        self.pts = 0
        self.hp = 3

    def generate_tree(self):
        Knot("assets/knot.png", [(850/2) - 37.5, 30], 100, 0, self.all_sprites)
        Knot("assets/knot.png", [200, 150], 100, 1, self.all_sprites)
        Knot("assets/knot.png", [630 - 37.5, 150], 100, 1, self.all_sprites)
        Knot("assets/knot.png", [95, 320], 100, 2, self.all_sprites)
        Knot("assets/knot.png", [280, 320], 100, 2, self.all_sprites)
        Knot("assets/knot.png", [495, 320], 100, 2, self.all_sprites)
        Knot("assets/knot.png", [680, 320], 100, 2, self.all_sprites)
        Knot("assets/knot.png", [25, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [140, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [220, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [330, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [440, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [550, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [620, 500], 100, 3, self.all_sprites)
        Knot("assets/knot.png", [740, 500], 100, 3, self.all_sprites)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.all_sprites.draw(self.window)