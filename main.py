import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platform")

# temporary background
width, height = 1000, 850
fps = 60
# this will determine the speed of the character
player_vel = 5

window = pygame.display.set_mode((width, height))

script_dir = os.path.dirname(__file__) 

# to help with directory to retrive the image for the background
image_path = os.path.join(script_dir, 'assets', 'tempbg.png')
background_image = pygame.image.load(image_path).convert()
background_image = pygame.transform.scale(background_image, (width, height))

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(background_image, (0, 0))

        pygame.display.flip() # Update the full display Surface to the screen

    pygame.quit()
    quit()


if __name__=="__main__":
    main(window)