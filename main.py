import pygame
import random
from settings import *



# Window Maker
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Fix It Later")
clock = pygame.time.Clock()


# Game Loop
running = True
while running:
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    clock.tick(fps)
    screen.fill(black)
    pygame.display.flip()



