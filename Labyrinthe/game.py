import pygame
from pygame.locals import *

from config import *
from classes import *

pygame.init()

w = pygame.display.set_mode((450, 450))

def load (path):
    sprites = {}
    sprites['bg'] = pygame.image.load(path + "background.jpg").convert()
    sprites['start'] = pygame.image.load(path + "start.png").convert()
    sprites['wall'] = pygame.image.load(path + "wall.png").convert()
    sprites['banana'] = pygame.image.load(path + "banana.png").convert_alpha()
    sprites['dk_front'] = pygame.image.load(path + "dk_front.png").convert_alpha()
    sprites['dk_back'] = pygame.image.load(path + "dk_back.png").convert_alpha()
    sprites['dk_left'] = pygame.image.load(path + "dk_left.png").convert_alpha()
    sprites['dk_right'] = pygame.image.load(path + "dk_right.png").convert_alpha()
    return sprites

sprites = load(PATH_IMG)

dk = DK()

def free (pos, dir) :
    x = (pos[0] / 30)
    y = (pos[1] / 30)

    if dir == 'down':
        y += 1
    elif dir == 'up':
        y -= 1
    elif dir == 'left':
        x -= 1
    elif dir == 'right':
        x += 1
    with open("levels/1.txt", "r") as f:
        i = 0
        for line in f.readlines():
            j = 0
            for char in line.strip():
                if i == x and j == y and (char == '0' or char == 'a'):
                    return 1
                j += 1
            i += 1
    return 0

loop = 1
level = 0
goal = ()
while loop:
    level = 1
    pygame.time.Clock().tick(30)
    w.fill((0, 0, 0))

    w.blit(sprites['bg'], (0, 0))

    if level == 1:
        with open("levels/1.txt", "r") as f:
            i = 0
            for line in f.readlines():
                j = 0
                for char in line.strip():
                    if char == 'd':
                        w.blit(sprites['start'], (i*30, j*30))
                    elif char == 'm':
                        w.blit(sprites['wall'], (i*30, j*30))
                    elif char == 'a':
                        goal = (i*30, j*30)
                        w.blit(sprites['banana'], goal)
                    j += 1
                i += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                dk.move('bot', free(dk.getPos(), 'down'))
            elif event.key == K_UP:
                dk.move('top', free(dk.getPos(), 'up'))
            elif event.key == K_LEFT:
                dk.move('left', free(dk.getPos(), 'left'))
            elif event.key == K_RIGHT:
                dk.move('right', free(dk.getPos(), 'right'))

    w.blit(sprites[dk.getState()], dk.getPos())

    pygame.display.update()

    if dk.getPos() == goal:
        loop = 0
