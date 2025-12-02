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

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False)for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, "Assets", dir1, dir2)

    images_files = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image_name in images_files:
        full_image_path = join(path, image_name)

        try:
            sprite_sheet = pygame.image.load(join(path, full_image_path)).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image {image_name}: {e}")
            continue

        sprites = []

        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect =  pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0,0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            base_name = image_name.replace(".png", "").replace(".jpg", "")
            all_sprites[base_name + "_right"] = sprites
            all_sprites[base_name + "_left"] = flip(sprites)

        else:
            all_sprites[image_name.replace(".png", "")] = sprites

    return all_sprites

def get_block(size):
    path = join("Assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

script_dir = os.path.dirname(__file__) 

# to help with directory to retrive the image for the background
image_path = os.path.join(script_dir, 'Assets', 'tempbg.png')
background_image = pygame.image.load(image_path).convert()
background_image = pygame.transform.scale(background_image, (width, height))

#it'll help the sprites collision for this
class Player(pygame.sprite.Sprite):
   color = (255, 0, 0)
   gravity = 1
   sprites = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True) #name of the character here between "" and the MainCharacters is for the directory folder
   animation_delay = 3 # changes the speed of the sprites movements
   

   def __init__(self, x, y, width, height):
        super().__init__()
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

   def move(self, dx,dy):
       self.rect.x += dx
       self.rect.y += dy

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
       # self.y_vel += min(1, (self.fall_count / fps) * self.gravity)
       self.move(self.x_vel, self.y_vel)

       self.fall_count += 1
       self.update_sprite()

   def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count // self.animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

   def update(self):
       self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
       self.mask = pygame.mask.from_surface(self.sprite)


   def draw(self, win):
       win.blit(self.sprite, (self.rect.x, self.rect.y))

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x,  y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win):
       win.blit(self.image, (self.rect.x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = load_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(player_vel)
    if keys[pygame.K_RIGHT]:
         player.move_right(player_vel)

def main(window):
    clock = pygame.time.Clock()
    player = Player(100, 100, 50, 50)
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(background_image, (0, 0))
        player.loop(fps)
        handle_move(player)
        player.draw(window)# DO NOT REMOVE THIS IT FIXED ISSUE OF IT APPEARING 
        pygame.display.flip() # Update the full display Surface to the screen

    pygame.quit()
    quit()


if __name__=="__main__":
    main(window)