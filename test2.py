import sys
import time
import pygame
from pygame.locals import *


pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Animations')

DOWN_LEFT = 'downleft'
DOWN_RIGHT = 'downright'
UP_LEFT = 'upleft'
UP_RIGHT = 'upright'

# how many pixels each block should move at each iteration
MOVE_SPEED = 4

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# creating a block data structures
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UP_RIGHT}
b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir': UP_LEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWN_LEFT}
boxes = [b1, b2, b3]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # fill window surface
    window_surface.fill(WHITE)

    for b in boxes:
        # moving a block data structure
        if b['dir'] == DOWN_LEFT:
            b['rect'].left -= MOVE_SPEED
            b['rect'].top += MOVE_SPEED
        if b['dir'] == DOWN_RIGHT:
            b['rect'].left += MOVE_SPEED
            b['rect'].top += MOVE_SPEED
        if b['dir'] == UP_LEFT:
            b['rect'].left -= MOVE_SPEED
            b['rect'].top -= MOVE_SPEED
        if b['dir'] == UP_RIGHT:
            b['rect'].left += MOVE_SPEED
            b['rect'].top -= MOVE_SPEED

        # check if the block has moved outside the window
        if b['rect'].top < 0:
            # passing the block through the upper boundary
            if b['dir'] == UP_LEFT:
                b['dir'] = DOWN_LEFT
            if b['dir'] == UP_RIGHT:
                b['dir'] = DOWN_RIGHT
        if b['rect'].bottom > WINDOW_HEIGHT:
            # passing the block through the bottom boundary
            if b['dir'] == DOWN_LEFT:
                b['dir'] = UP_LEFT
            if b['dir'] == DOWN_RIGHT:
                b['dir'] = UP_RIGHT
        if b['rect'].left < 0:
            # passing the block through the left boundary
            if b['dir'] == DOWN_LEFT:
                b['dir'] = DOWN_RIGHT
            if b['dir'] == UP_LEFT:
                b['dir'] = UP_RIGHT
        if b['rect'].right > WINDOW_WIDTH:
            # passing the block through the right boundary
            if b['dir'] == DOWN_RIGHT:
                b['dir'] = DOWN_LEFT
            if b['dir'] == UP_RIGHT:
                b['dir'] = UP_LEFT

        # creating a block on the surface
        pygame.draw.rect(window_surface, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(0.02)
