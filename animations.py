from game import *
from spritesheet import SpriteSheet
import pygame
from constants import *
pygame.init()

class Dead_duck:
    def __init__(self,x,y):
        self.deadDuck = SpriteSheet("dead_duck.png")
        self.frames = []
        self.image = self.deadDuck.get_image(85,0,40,70)
        self.frames.append(self.image)
        self.image = self.deadDuck.get_image(125,0,40,70)
        self.frames.append(self.image)
        self.image = self.deadDuck.get_image(165, 0, 40, 70)
        self.frames.append(self.image)
        self.image = self.deadDuck.get_image(0,0,70,70)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change = 8
    def fall(self):
        self.rect.y += self.change
        pos = self.rect.x
        frame = (pos // 30) % len(self.frames)
        if self.rect.y > 400:
            self.change = 0
            dog = pygame.image.load("dog.png").convert_alpha()
            screen.blit(dog,(self.rect.x,self.rect.y))
        self.image = self.frames[frame]
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

