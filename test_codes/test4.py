import sys
import random
import pygame
from pygame.locals import *


pygame.init()
main_clock = pygame.time.Clock()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Sprites with sounds')

WHITE = (255, 255, 255)

# Creation of the player and food data structures
player = pygame.Rect(300, 100, 40, 40)
player_image = pygame.image.load('images/chimp.bmp')
player_stretched_image = pygame.transform.scale(player_image, (40, 40))
food_image = pygame.image.load('images/bomb.gif')
FOOD_SIZE = 20

foods = []
for i in range(20):
    foods.append(
        pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE),
                    random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)
    )

food_counter = 0
NEW_FOOD = 40


move_left = False
move_right = False
move_up = False
move_down = False

MOVE_SPEED = 6

# music setting
pick_up_sound = pygame.mixer.Sound('images/boom.wav')
pygame.mixer.music.load('images/house_lo.mp3')
pygame.mixer.music.play(-1, 0.0)
music_playing = True


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            # Change keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_RIGHT or event.key == K_d:
                move_right = True
                move_left = False
            if event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True
            if event.key == K_DOWN or event.key == K_s:
                move_down = True
                move_up = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                player.left = random.randint(0, WINDOW_WIDTH - player.width)
            if event.key == K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                music_playing = not music_playing

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1] - 10, FOOD_SIZE, FOOD_SIZE))

    food_counter += 1
    if food_counter >= NEW_FOOD:
        # add new food
        food_counter = 0

        foods.append(
            pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE),
                        random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)
        )

    window_surface.fill(WHITE)

    # player movement
    if move_down and player.bottom < WINDOW_HEIGHT:
        player.top += MOVE_SPEED
    if move_up and player.top > 0:
        player.top -= MOVE_SPEED
    if move_left and player.left > 0:
        player.left -= MOVE_SPEED
    if move_right and player.right < WINDOW_WIDTH:
        player.right += MOVE_SPEED

    # display block on the surface
    window_surface.blit(player_stretched_image, player)

    # check if a player has crossed with any food blocks
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            player_stretched_image = pygame.transform.scale(player_image, (player.width, player.height))

            if music_playing:
                pick_up_sound.play()

    # display food
    for food in foods:
        window_surface.blit(food_image, food)

    pygame.display.update()
    main_clock.tick(40)
