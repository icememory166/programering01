import pygame, sys # import pygame and sys

clock = pygame.time.Clock() # set up the clock

from pygame.locals import * # import pygme modules
pygame.init() # initiates pygame

pygame.display.set_caption('Test game') # set window name

WINDOW_SIZE = (400,400) # set window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiates the window

player_image = pygame.image.load('player.png')

moving_right = False
moving_left = False

player_location = [50,50]
player_y_momentum = 0

player_rect = pygame.rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())

while True: # game loop
    screen.fill((146,244,255))

    screen.blit(player_image,player_location)

    if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

        player_rect.x = player_location[0]
        player_rect.y = player_location[1]

    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps
