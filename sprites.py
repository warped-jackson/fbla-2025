import pygame

from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self.layer = Player_Layer
        self.groups = self.game.all_sprites
        pygame.sprites.Sprites__init__(self,self.groups)

        self.x = x * Tilesize
        self.y = y * Tilesize
        self.width = Tilesize
        self.height = Tilesize

        self.image = pygame.Surface([self.width,self,height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = self.y
        self.rect.x = self.x