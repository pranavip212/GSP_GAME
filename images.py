import pygame
from constants import *

screen = pygame.display.set_mode((800, 600))
mila_size = (195, 520)

# backgrounds
bedroom = pygame.image.load('assets/images/bedroom.png').convert()
bedroom = pygame.transform.scale(bedroom, (WIDTH, HEIGHT))

day_hallway = pygame.image.load('assets/images/day_hallway.png').convert()
day_hallway = pygame.transform.scale(day_hallway, (WIDTH, HEIGHT))
hallway_lit = pygame.image.load('assets/images/hallway_lit.png').convert()
hallway_lit = pygame.transform.scale(hallway_lit, (WIDTH, HEIGHT))
hallway_dark = pygame.image.load('assets/images/hallway_dark.png').convert()
hallway_dark = pygame.transform.scale(hallway_dark, (WIDTH, HEIGHT))

maze = pygame.image.load('assets/images/maze.png').convert()
maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))
maze_above = pygame.image.load('assets/images/maze.png').convert()
maze_above = pygame.transform.scale(maze_above, (WIDTH, HEIGHT))

# character sprites
zombie = pygame.image.load("assets/images/zombie_jaw.png").convert_alpha()
zombie = pygame.transform.scale(zombie, (300, 300))

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

mila_sprite_idle = pygame.image.load("assets/images/mila_standing_clear_OLD.png").convert_alpha()
mila_sprite_idle = pygame.transform.scale(mila_sprite_idle, (700, 500))
mila_sprite_walk_1 = pygame.image.load("assets/images/mila_standing_clear_OLD.png").convert_alpha()
mila_sprite_walk_1 = pygame.transform.scale(mila_sprite_walk_1, (700, 500))
mila_sprite_walk_2 = pygame.image.load("assets/images/mila_standing_clear_OLD.png").convert_alpha()
mila_sprite_walk_2 = pygame.transform.scale(mila_sprite_walk_2, (700, 500))