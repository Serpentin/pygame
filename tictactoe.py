import pygame
from pygame.locals import *

import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

screen = (600, 450)
case = (screen[0]/3, screen[1]/3)

pygame.init()

w = pygame.display.set_mode(screen, RESIZABLE)

class Game:
    def __init__(self):
        self.clear()

    def draw(self):
        for i in range(0, len(self.state)):
            for j in range (0, len(self.state[i])):
                if self.state[i][j] == '0':
                    r = pygame.rect.Rect(i*case[0], j*case[1], case[0], case[1])
                    pygame.draw.rect(w, BLACK, r, 4)
                elif self.state[i][j] == 'o':
                    r = pygame.rect.Rect(i*case[0], j*case[1], case[0], case[1])
                    pygame.draw.rect(w, BLACK, r, 4)
                    pygame.draw.circle(w, BLACK, (int(case[0]/2 + 2*i*case[0]/2), int(case[1]/2 + 2*j*case[1]/2)), int(case[0]/2 if case[0] <= case[1] else case[1]/2), 2)
                elif self.state[i][j] == 'x':
                    r = pygame.rect.Rect(i*case[0], j*case[1], case[0], case[1])
                    pygame.draw.rect(w, BLACK, r, 4)
                    pygame.draw.line(w, BLACK, ((i+1)*case[0], j*case[1]), (i*case[0], (j+1)*case[1]), 2)
                    pygame.draw.line(w, BLACK, (i*case[0], j*case[1]), ((i+1)*case[0], (j+1)*case[1]), 2)

    def clear(self):
        self.state = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ]
        self.next = 'o'

    def win(self, player):
        print (player, ' WON!')
        self.clear()

    def check(self):
        for i in range (0, len(self.state)):

            if self.state[i].count('0') == 0:
                if self.state[i].count(self.state[i][0]) == len(self.state[i]):
                    self.win(self.state[i][0])

            j = 0
            if self.state[j][i] == self.state[j+1][i] == self.state[j+2][i] and self.state[j][i] != '0':
                self.win(self.state[i][j])

        if self.state[0][0] == self.state[1][1] == self.state[2][2] and self.state[0][0] != '0':
            self.win(self.state[1][1])
        elif self.state[2][0] == self.state[1][1] == self.state[0][2] and self.state[2][0] != '0':
            self.win(self.state[1][1])

    def play(self, pos):

        x = math.floor(pos[0] / case[0])
        y = math.floor(pos[1] / case[1])

        if (self.state[x][y] == '0'):
            self.state[x][y] = self.next

        self.next = 'o' if self.next == 'x' else 'x'

        self.check()


g = Game()

loop = 1
while loop:

    pygame.time.Clock().tick(30)
    w.fill(WHITE)

    g.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            g.play(event.pos)
        if event.type == VIDEORESIZE:
            screen = (event.w, event.h)
            case = (screen[0]/3, screen[1]/3)
            w = pygame.display.set_mode(screen, RESIZABLE)
