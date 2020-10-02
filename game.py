import pygame
import random
from constants import *
from our_duck import Duck
from spritesheet import SpriteSheet
from aim import *
from highscore import Highscore
from os import path
hs_file = "score.txt"
from animations import *
pygame.init()


def load_data():
    global file, hs
    file = path.dirname(__file__)
    with open(path.join(file, hs_file), "r") as f:
        try:
            hs = int(f.read())
        except:
            hs = 0

class Game:
    def __init__(self):
        load_data()
    def play(self,num,s):
        ducks = pygame.sprite.Group()
        self.score = s
        n = num
        for d in range(n):
            duck = Duck(random.randint(0,750),random.randint(0,300))
            ducks.add(duck)
            shot = False
            deaD = False
        running = True
        clock = pygame.time.Clock()
        ammo = 3
        time = 225
        while running:
            screen.blit(bg,(0,0))
            x,y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            Crosshair(x,y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shot = True
                    ammo -= 1
                if event.type == pygame.MOUSEBUTTONUP:
                    shot = False
            hit = pygame.sprite.spritecollide(Crosshair(x,y),ducks,False)
            if hit and shot == True:
                for duck in hit:
                    dead = Dead_duck(duck.rect.x,duck.rect.y)
                    deaD = True
                    ammo = 3
                    self.score += 500
                    duck.kill()
            if deaD:
                dead.fall()
                dead.draw()
            if len(ducks) == 0:
                pygame.time.wait(1000)
                n += 1
                Game.play(Game,n,self.score)
            if ammo == 0:
                screen.fill((0,0,0))
                font = pygame.font.SysFont("Arial",50)
                text = font.render("Fly Away",True,(0,0,0))
                screen.blit(text,(300,250))
                pygame.display.update()
                pygame.time.wait(1000)
                Game.main_menu(Game)

            font = pygame.font.SysFont("Courier New", 25)
            text1 = font.render("Ammo: " + str(ammo), False, (255,255,255))
            text2 = font.render("Ducks left:"  + str(len(ducks)), False, (255,255,255))
            text3 = font.render("Score: " + str(s), False, (255,255,255))
            text4 = font.render("High Score: " + str(hs), False, (255, 255, 255))
            screen.blit(text1,(75,525))
            screen.blit(text2,(325,525))
            screen.blit(text3,(625,525))
            pygame.display.update()
            time -= 1
            if time <= 0:
                screen.fill((0, 0, 0))
                font = pygame.font.SysFont("Arial", 50)
                text = font.render("Fly Away", True, (0, 0, 0))
                screen.blit(text, (300, 250))
                pygame.display.update()
                pygame.time.wait(1000)
                Game.main_menu()
            ducks.update()
            ducks.draw(screen)
            pygame.display.flip()
            clock.tick(60)

    def main_menu(self):
        load_data()
        screen.fill((0,0,0))
        font = pygame.font.SysFont("Courier New",50)
        text = font.render("Duck Hunt", False, (255,255,255))
        screen.blit(text,(400,300))
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Game.play(Game,1,0)




