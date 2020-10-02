import pygame
pygame.init()

screen = pygame.display.set_mode([800, 600])
bg = pygame.image.load("duck_hunt_bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (800, 600))
icon = pygame.image.load("icon.png")
pygame.display.set_caption("Duck Hunt")
pygame.display.set_icon(icon)
