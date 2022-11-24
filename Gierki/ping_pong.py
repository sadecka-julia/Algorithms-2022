

import pygame
from pygame.locals import *

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("E:\POBRANE\PobranyPython\BB_Resources\Resources\images\dude.png")
grass = pygame.image.load("E:\POBRANE\PobranyPython\BB_Resources\Resources\images\grass.png")

while 1:
    screen.fill(0)
    for x in range(width/grass.get_width()):
        for y in range(height/grass.get_height()):
            screen.blit(grass,(x*100, y*100))
    screen.blit(player, (100, 300))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

