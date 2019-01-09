import sys
import pygame
from pygame.locals import *


pygame.init()

# window setting
window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 25)

# add font
basic_font = pygame.font.SysFont(None, 48)

# add text
text = basic_font.render('Hello, World!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window.get_rect().centerx
text_rect.centery = window.get_rect().centery

# fill window surface
window.fill(WHITE)

# add polygon, lines and etc
pygame.draw.polygon(window, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

pygame.draw.line(window, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(window, BLUE, (120, 60), (60, 120))
pygame.draw.line(window, BLUE, (60, 120), (120, 120), 4)

pygame.draw.circle(window, BLUE, (300, 50), 20, 0)

pygame.draw.ellipse(window, RED, (300, 250, 40, 80), 1)

pygame.draw.rect(window, RED, (text_rect.left - 20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))

# get list of pixels
pix_array = pygame.PixelArray(window)
pix_array[480][380] = BLACK
del pix_array

# blit() adds text into window surface
window.blit(text, text_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
