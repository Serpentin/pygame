import pygame
from pygame.locals import *
from math import *

import random

pygame.init()

SCREEN_SIZE = (600, 600)
WHITE = (255, 255, 255)
SIZE = 20

w = pygame.display.set_mode(SCREEN_SIZE)

class Game:

    def draw(self, elements):
        for element in elements:
            pygame.draw.rect(w, element[1], element[0])

    def render(self, elements):
        for element in elements:
            self.draw(element)


class Snake:

    def __init__(self, pos, length):
        self.queue = []
        self.old_queue = []
        self.state = 'down'
        self.length = length
        for i in range (0, self.length):
            self.queue.append([pygame.rect.Rect(pos[0]*SIZE, pos[1]*SIZE, SIZE, SIZE), WHITE])
        self.old_queue = self.queue

    def eat(self, pos):
        for i in range (0, len(self.queue)):
            if self.queue[i][0].collidepoint(pos[0], pos[1]):
                self.queue.append([pygame.rect.Rect(self.queue[-1][0].x*SIZE, self.queue[-1][0].y*SIZE, SIZE, SIZE), WHITE])
                return 1
        return 0

    def free(self, first, queue, dir):

        if dir == 'up':
            for i in range (1, len(queue)):
                if queue[i][0].collidepoint(first.x, first.y-30):
                    return 0
        elif dir == 'down':
            for i in range (1, len(queue)):
                if queue[i][0].collidepoint(first.x, first.y+30):
                    return 0
        elif dir == 'left':
            for i in range (1, len(queue)):
                if queue[i][0].collidepoint(first.x-30, first.y):
                    return 0
        elif dir == 'right':
            for i in range (1, len(queue)):
                if queue[i][0].collidepoint(first.x+30, first.y):
                    return 0
        return 1



    def move(self, dir):
        if self.free(self.queue[0][0], self.queue, dir) == 1:
            if self.state != dir:
                self.state = dir

            new_queue = []

            if self.state == 'down':
                new_queue.append([self.queue[0][0].move(0, SIZE), WHITE])
            elif self.state == 'up':
                new_queue.append([self.queue[0][0].move(0, -SIZE), WHITE])
            elif self.state == 'left':
                new_queue.append([self.queue[0][0].move(-SIZE, 0), WHITE])
            elif self.state == 'right':
                new_queue.append([self.queue[0][0].move(SIZE, 0), WHITE])

            if new_queue[0][0].x >= SCREEN_SIZE[0]:
                new_queue[0][0].x = 0
            if new_queue[0][0].x < 0:
                new_queue[0][0].x = SCREEN_SIZE[0] - SIZE
            if new_queue[0][0].y >= SCREEN_SIZE[1]:
                new_queue[0][0].y = 0
            if new_queue[0][0].y < 0:
                new_queue[0][0].y = SCREEN_SIZE[1] - SIZE

            for i in range (1, len(self.queue)):
                new_queue.append(self.old_queue[i-1])

            self.queue = new_queue
            self.old_queue = self.queue

class Apple:
    def __init__(self):
        self.generate()
    def generate(self):
        self.pos = [random.randint(0, SCREEN_SIZE[0]/SIZE-1)*SIZE, random.randint(0, SCREEN_SIZE[1]/SIZE-1)*SIZE]
        self.rect = [pygame.rect.Rect(self.pos[0], self.pos[1], SIZE, SIZE), (255, 0, 0)]


game = Game()
snake = Snake([round((SCREEN_SIZE[0]/SIZE)/2), round((SCREEN_SIZE[1]/SIZE)/2)], 50)
print([round(SCREEN_SIZE[0]/SIZE), round(SCREEN_SIZE[1]/SIZE)])
apple = Apple()

loop = 1
while loop:

    pygame.time.Clock().tick(10)
    w.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                snake.move('up')
            elif event.key == K_DOWN:
                snake.move('down')
            elif event.key == K_LEFT:
                snake.move('left')
            elif event.key == K_RIGHT:
                snake.move('right')

    snake.move(snake.state)

    elements = [snake.queue, [apple.rect]]
    game.render(elements)

    if snake.eat(apple.pos):
        apple.generate()

    pygame.display.update()
    if not snake.free(snake.queue[0][0], snake.queue, snake.state):
        loop = 0
