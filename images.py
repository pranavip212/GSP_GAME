import pygame
from constants import *

screen = pygame.display.set_mode((800, 600))

# source: https://www.artstation.com/artwork/r9keZL
bedroom = pygame.image.load('assets/images/bedroom.png').convert()
bedroom = pygame.transform.scale(bedroom, (WIDTH, HEIGHT))

day_hallway = pygame.image.load('assets/images/day_hallway.png').convert()
day_hallway = pygame.transform.scale(day_hallway, (WIDTH, HEIGHT))

# source: https://pxlart.com/p/AYi7UcS6Q9W5EZUu4SYw/nostalgic-16-bit-pixel-art-scene-of-a, edited by Chelsea
hallway_lit = pygame.image.load('assets/images/hallway_lit.png').convert()
hallway_lit = pygame.transform.scale(hallway_lit, (WIDTH, HEIGHT))
hallway_dark = pygame.image.load('assets/images/hallway_dark.png').convert()
hallway_dark = pygame.transform.scale(hallway_dark, (WIDTH, HEIGHT))

# source: https://cargocollective.com/urituchman/Pixel-Art, edited by Chelsea
breakfast = pygame.image.load('assets/images/breakfast.png').convert()
breakfast = pygame.transform.scale(breakfast, (WIDTH, HEIGHT))
breakfast_gray = pygame.image.load('assets/images/breakfast_gray.png').convert()
breakfast_gray = pygame.transform.scale(breakfast_gray, (WIDTH, HEIGHT))

plate_of_bacon = pygame.image.load('assets/images/plate_of_bacon.png').convert()
plate_of_bacon = pygame.transform.scale(plate_of_bacon, (WIDTH, HEIGHT))

# source: https://ukpurgatorio.miraheze.org/wiki/E-2:_Palace_of_Black_Spires, edited by Chelsea
maze = pygame.image.load('assets/images/maze.png').convert()
maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))

# source: https://www.magnific.com/premium-ai-image/pixel-art-depicting-stark-black-brick-wall-against-pristine-white-backdrop_342271985.htm
maze_ground = pygame.image.load('assets/images/maze_ground.png').convert()
maze_ground = pygame.transform.scale(maze_ground, (1000, 700))

# source: https://www.vecteezy.com/vector-art/40531762-green-exit-sign-in-pixel-art-style
target_sprite = pygame.image.load("assets/images/target_sprite.png").convert_alpha()
target_sprite = pygame.transform.scale(target_sprite, (360, 360))

# made by Chelsea
player_sprite = pygame.image.load("assets/images/player_sprite.png").convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, (130, 130))
mila_sprite = pygame.image.load("assets/images/mila_sprite.png").convert_alpha()
mila_sprite = pygame.transform.scale(mila_sprite, (180, 150))

# source: https://www.vecteezy.com/png/72637392-pixelated-zombie-head-undead-horror-in-retro-style-549
zombie = pygame.image.load("assets/images/zombie_jaw.png").convert_alpha()
zombie = pygame.transform.scale(zombie, (300, 300))

# source: https://x.com/9E0_D0/status/1456289863679070209, edited by Chelsea
zombie_hand = pygame.image.load("assets/images/zombie_hand.png").convert_alpha()
zombie_hand = pygame.transform.scale(zombie_hand, (414, 372))

# source: https://www.reddit.com/r/PixelArt/comments/v8d4e3/is_she_too_cute_to_be_a_horror_game_protagonist/, edited by Chelsea
mila_size = (270, 720)
mila_normal_lit = pygame.image.load("assets/images/mila_normal_lit.png").convert_alpha()
mila_normal_lit = pygame.transform.scale(mila_normal_lit, mila_size)
mila_happy_lit = pygame.image.load("assets/images/mila_happy_lit.png").convert_alpha()
mila_happy_lit = pygame.transform.scale(mila_happy_lit, mila_size)
mila_pensive_lit = pygame.image.load("assets/images/mila_pensive_lit.png").convert_alpha()
mila_pensive_lit = pygame.transform.scale(mila_pensive_lit, mila_size)
mila_normal_dark = pygame.image.load("assets/images/mila_normal_dark.png").convert_alpha()
mila_normal_dark = pygame.transform.scale(mila_normal_dark, mila_size)
mila_happy_dark = pygame.image.load("assets/images/mila_happy_dark.png").convert_alpha()
mila_happy_dark = pygame.transform.scale(mila_happy_dark, mila_size)
mila_pensive_dark = pygame.image.load("assets/images/mila_pensive_dark.png").convert_alpha()
mila_pensive_dark = pygame.transform.scale(mila_pensive_dark, mila_size)
mila_tears_dark = pygame.image.load("assets/images/mila_tears_dark.png").convert_alpha()
mila_tears_dark = pygame.transform.scale(mila_tears_dark, mila_size)
mila_silhouette = pygame.image.load("assets/images/mila_silhouette.png").convert_alpha()
mila_silhouette = pygame.transform.scale(mila_silhouette, mila_size)

# source: https://es.pinterest.com/pin/849702654685205639/
kitchen = pygame.image.load("assets/images/kitchen.png").convert_alpha()
kitchen = pygame.transform.scale(kitchen, (WIDTH, HEIGHT))