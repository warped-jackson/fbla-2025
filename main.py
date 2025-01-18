import pygame
import random
from settings import *

class Game:
    def __init(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Fix It Later")
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        all_sprites = pygame.sprite.group()

def run(self):
    self.playing = True
    while self.playing:
        self.clock.tick(fps)
        self.update()
        self.events()
        self.draw()


def update(self):
    pass

def events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if self.playing:
                self.playing = False
            running = False


def draw(self):
    screen.fill(red)
    all_sprites.draw(screen)
    pygame.display.flip()


def show_go_screen(self):
    pass

g = Game()
#g.show_start_screen
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
# Window Maker
#pygame.display.flip()



