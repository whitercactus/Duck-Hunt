import pygame
import random
from constants import *
from our_duck import *
from spritesheet import SpriteSheet
from aim import Crosshair
from game import Game
pygame.init()
if __name__ == "__main__":
    Game.main_menu(Game())
