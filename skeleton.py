import pygame
import os
from pygame.locals import *

# CONSTANTES

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WINDOW = (450, 450)
TITLE = "Game"
FPS = 30

IMG_PATH = "platformer/"

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



def render():
    screen.fill(BLACK)
    # YOUR LOGIC

    pygame.display.update()


def main():

    load(IMG_PATH)

    exit = 0
    while not exit:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit = 1

        render()
        clock.tick(FPS)


    pygame.quit()
    quit()

main()
