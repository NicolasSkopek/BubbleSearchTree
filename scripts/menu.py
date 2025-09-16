import sys
import pygame

from scripts.scene import Scene
from scripts.obj import Obj

class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.next_scene()

    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

