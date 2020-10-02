import pygame
from game import Game
from constants import *
from spritesheet import SpriteSheet
pygame.init()

class Duck(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        sprite_sheet = SpriteSheet("duck.png")
        self.frames = []
        image = sprite_sheet.get_image(0,0,75,75)
        self.frames.append(image)
        image = sprite_sheet.get_image(75, 0, 75, 75)
        self.frames.append(image)
        image = sprite_sheet.get_image(150, 0, 75, 75)
        self.frames.append(image)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 7
        self.change_y = 5
    def update(self):
        pos = self.rect.x
        frame = (pos // 30) % len(self.frames)
        self.image = self.frames[frame]
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            self.change_x *= -1
        if self.rect.x > 800:
            self.change_x *= -1
        if self.rect.y < 0:
            self.change_y *= -1
        if self.rect.y > 400:
            self.change_y *= -1
    def draw(self):
        Game.screen.blit(self.image,(self.rect.x,self.rect.y))






        
