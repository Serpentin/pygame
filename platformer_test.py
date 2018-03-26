import pygame
import os
from pygame.locals import *

# CONSTANTES

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WINDOW = (1200, 600)
TITLE = "platformer_test"
FPS = 60

IMG_PATH = "platformer_test/"

# INITIALISATION

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW)
pygame.display.set_caption(TITLE)
pygame.key.set_repeat(10, 10)

images = []

def load(img_path):
    # Loading images
    for filename in os.listdir(img_path):
        ext = filename.split('.')[-1]
        if ext == ('png' or 'jpg' or 'jpeg'):
            if ext == 'png':
                images.append(pygame.image.load(img_path + filename).convert_alpha())
            else:
                images.append(pygame.image.load(img_path + filename).convert())


def text(content, color, pos, size=15, font_name="arial", bold=0, italic=0):
    font = pygame.font.SysFont(font_name, size, bold, italic)
    label = font.render(content, 1, color)
    screen.blit(label, pos)

class Player:
    def __init__(self):
        self.right = (30, 304, 95, 450)
        self.left = (123, 304, 195, 450)
        self.walk_right = ((23, 0, 88, 150), (120, 0, 88, 150), (210, 0, 88, 150), (338, 0, 88, 150), (430, 0, 88, 150), (523, 0, 88, 150))
        self.walk_left = ((23, 150, 88, 150), (120, 150, 88, 150), (210, 150, 88, 150), (318, 150, 108, 150), (430, 150, 88, 150), (523, 150, 88, 150))
        self.current = self.right
        self.pos = [0, 0]

    def render(self):
        screen.blit(images[0], self.pos, self.current)
p = Player()

def render():
    screen.fill(WHITE)
    # CHANGES
    p.render()
    pygame.display.update()

i = 0
go = 0
def main(i, go):

    load(IMG_PATH)

    exit = 0
    while not exit:


        for event in pygame.event.get():
            if event.type == QUIT:
                exit = 1
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    p.pos[0] += 5
                    if go == 6:
                        if i > 5:
                            i = 0
                        p.current = p.walk_right[i]
                        i += 1
                elif event.key == K_LEFT:
                    p.pos[0] -= 5
                    if go == 6:
                        if i > 5:
                            i = 0
                        p.current = p.walk_left[i]
                        i += 1
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    p.current = p.right
                    i = 0
                if event.key == K_LEFT:
                    p.current = p.left
                    i = 0

        render()
        clock.tick(FPS)
        if go < 6:
            go += 1
        else:
            go = 0

    pygame.quit()

main(i, go)
