import pygame
from scripts.startgame import *
from scripts.api import start_api_thread

if __name__ == "__main__":
    start_api_thread()

    start_game = StartGame()
    start_game.run()
