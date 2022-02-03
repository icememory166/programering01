import pygame, sys # import pygame and sys

clock = pygame.time.Clock() # set up the clock

from pygame.locals import * # import pygme modules
pygame.init() # initiates pygame

pygame.display.set_caption('Test game') # set window name

WINDOW_SIZE = (400,400) # set window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiates the window

player_image = pygame.image.load('player.png')

while True: # game loop

    screen.blit(player_image,(50,50))

    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script


    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps
