import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display. set_mode((winWidth, winHeight))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font('Arial',32)

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.player = Player(self,1,2)

        self.player = Player(self,1,2)


def events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.playing = False
            self.running + False
def update(self):
    self.all_sprites.update()

def main(self):
    while self.playing:
        self.events()
        self.updates()
        self.draw()


def draw(self):
    self.screen.fill(BLACK)
    self.all_sprites.draw(self.screen)
    self.clock.tick(FPS)
    pygame.display.update

def game_over(self):
    pass
def intro_screen(self):
    pass







g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()