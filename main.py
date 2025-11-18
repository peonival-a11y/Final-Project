import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platform")

# temporary background
bg_color = (255, 255, 255)
width, height = 1000, 850
fps = 60
# this will determine the speed of the character
player_vel = 5

window = pygame.display.set_mode((width, height))

#important to have the directory connected to this
def get_background(name):
    image = pygame.image.load(join("Assets", "background", 'tempng.jpg'))


def draw(window, background):
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background = get_background("tempbg.jpg")
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break




if __name__=="__main__":
    main(window)