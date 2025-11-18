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

#it'll help the sprites collision for this
class Player(pygame.sprite.Sprite):
   color = (255, 0, 0)
   def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left" # will shoq the direction of the character
        self.animation_count = 0  #change the animation frames
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
    #revise code on why the indentation is not working properly
    def move(self, dx, dy):
       self.react.x +- dx
       self.react.y +- dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel) # focusing on how it moves for now

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def draw(player):
        player.draw(window)

        pygame.display.update()

def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(player_vel)
    if keys[pygame.K_RIGHT]:
         player.move_right(player_vel)

def main(window):
    clock = pygame.time.Clock()
    player = player(100, 100, 50, 50)
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