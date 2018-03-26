import pygame
import os
from pygame.locals import *

import math

# CONSTANTES

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WINDOW = (800, 800)
TITLE = "SHOOTER"
FPS = 60

IMG_PATH = "shooter/"

# INITIALISATION

pygame.init()

def load(img_path):
    # Loading images
    for filename in os.listdir(img_path):
        ext = filename.split('.')[-1]
        name = filename.split('.')[0]
        if ext == ('png' or 'jpg' or 'jpeg'):
            if ext == 'png':
                images[name] = pygame.image.load(img_path + filename).convert_alpha()
            else:
                images[name] = pygame.image.load(img_path + filename).convert()



clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW)
pygame.display.set_caption(TITLE)
# pygame.display.set_icon(icon)


images = {}
fonts = {}

def text(content, color, pos, size=15, font_name="arial", bold=0, italic=0):

    params = font_name + '/' + str(size) + '/' + str(bold) + '/' + str(italic)
    if not params in fonts:
        fonts[params] = pygame.font.SysFont(font_name, size, bold, italic)

    label = fonts[params].render(content, 1, color)
    screen.blit(label, pos)

class Player:
    def __init__(self):
        self.pos = [WINDOW[0]/2, WINDOW[1]/2]
        self.position = [WINDOW[0]/2, WINDOW[1]/2]
        self.cooldown = 20
        self.loaded = 1
        self.speed = 9
        self.powerspeed = 3

    def render(self, mouse_pos, move):
        self.angle = 360-math.atan2(mouse_pos[1]-self.pos[1],mouse_pos[0]-self.pos[0])*180/math.pi
        self.image = pygame.transform.rotozoom(images['player'], self.angle, 1.0)


        self.position[0] += move[0]
        self.position[1] += move[1]
        self.pos = self.image.get_rect(center=(self.position[0], self.position[1]))
        screen.blit(self.image, self.pos)

def render(player, mouse_pos, bullets, move):
    screen.fill(BLACK)

    player.render(mouse_pos, move)

    for bullet in bullets:

        if bullet[0][0] > WINDOW[0] or bullet[0][0] < 0 or bullet[0][1] > WINDOW[1] or bullet[0][1] < 0:
            bullets.remove(bullet)
        else:
            screen.blit(images['bullet'], bullet[0])
            bullet[0][0] += 10 * math.cos(bullet[1])
            bullet[0][1] += 10 * math.sin(bullet[1])


    pygame.display.update()


def main():

    load(IMG_PATH)

    player = Player()
    bullets = []
    tick = 0
    move = [0, 0]

    exit = 0
    while not exit:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit = 1
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONDOWN:
                if player.loaded:
                    angle = math.atan2(mouse_pos[1] - player.pos[1], mouse_pos[0] - player.pos[0])
                    bullets.append([[player.pos[0] + 21 + math.cos(angle) * 30, player.pos[1] + 16 + math.sin(angle) * 30], angle])
                    player.loaded = 0
            if event.type == KEYDOWN:
                if event.key == K_d:
                    if move[0] < player.speed:
                        move[0] += player.powerspeed
                if event.key == 97:
                    if move[0] > -player.speed:
                        move[0] -= player.powerspeed
                if event.key == 119:
                    if move[1] > -player.speed:
                        move[1] -= player.powerspeed
                if event.key == K_s:
                    if move[1] < player.speed:
                        move[1] += player.powerspeed

        render(player, mouse_pos, bullets, move)

        clock.tick(FPS)
        tick += 1
        if tick == player.cooldown:
            player.loaded = 1
            tick = 0

    pygame.quit()
    quit()

main()
