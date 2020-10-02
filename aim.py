import pygame
from constants import *
pygame.init()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("crosshair.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image,(self.rect.x,self.rect.y))

