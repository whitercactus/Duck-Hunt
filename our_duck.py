import pygame
from constants import *
from spritesheet import SpriteSheet
pygame.init()

class Duck(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        sprite_sheet = SpriteSheet("duck.png")
        self.frames_r = []
        self.frames_l = []
        image = sprite_sheet.get_image(0,0,70,70)
        self.frames_r.append(image)
        image = sprite_sheet.get_image(70, 0, 70, 70)
        self.frames_r.append(image)
        image = sprite_sheet.get_image(140, 0, 70, 70)
        image = pygame.transform.flip(image,True,False)
        self.frames_l.append(image)
        image = sprite_sheet.get_image(0, 0, 75, 75)
        image = pygame.transform.flip(image, True, False)
        self.frames_l.append(image)
        image = sprite_sheet.get_image(75, 0, 75, 75)
        image = pygame.transform.flip(image, True, False)
        self.frames_l.append(image)
        image = sprite_sheet.get_image(150, 0, 75, 75)
        self.frames_r.append(image)
        self.image = self.frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 10
        self.change_y = 7
        self.dir = "r"
    def update(self):
        pos = self.rect.x
        if self.dir == "r":
            frame = (pos // 30) % len(self.frames_r)
            self.image = self.frames_r[frame]
        if self.dir == "l":
            frame = (pos // 30) % len(self.frames_l)
            self.image = self.frames_l[frame]
        if self.change_x == 10:
            self.dir = "r"
        if self.change_x == -10:
            self.dir = "l"
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            self.change_x *= -1
        if self.rect.x > 750:
            self.change_x *= -1
        if self.rect.y < 0:
            self.change_y *= -1
        if self.rect.y >= 300:
            self.change_y *= -1
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))