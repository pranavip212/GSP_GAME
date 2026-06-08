import pygame
from constants import *

screen = pygame.display.set_mode((800, 600))
mila_size = (270, 720)

# backgrounds
bedroom = pygame.image.load('assets/images/bedroom.png').convert()
bedroom = pygame.transform.scale(bedroom, (WIDTH, HEIGHT))

day_hallway = pygame.image.load('assets/images/day_hallway.png').convert()
day_hallway = pygame.transform.scale(day_hallway, (WIDTH, HEIGHT))
hallway_lit = pygame.image.load('assets/images/hallway_lit.png').convert()
hallway_lit = pygame.transform.scale(hallway_lit, (WIDTH, HEIGHT))
hallway_dark = pygame.image.load('assets/images/hallway_dark.png').convert()
hallway_dark = pygame.transform.scale(hallway_dark, (WIDTH, HEIGHT))

# source: https://cargocollective.com/urituchman/Pixel-Art, edited by Chelsea
breakfast = pygame.image.load('assets/images/breakfast.png').convert()
breakfast = pygame.transform.scale(breakfast, (WIDTH, HEIGHT))
breakfast_gray = pygame.image.load('assets/images/breakfast_gray.png').convert()
breakfast_gray = pygame.transform.scale(breakfast_gray, (WIDTH, HEIGHT))

maze = pygame.image.load('assets/images/maze.png').convert()
maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))
maze_above = pygame.image.load('assets/images/maze.png').convert()
maze_above = pygame.transform.scale(maze_above, (WIDTH, HEIGHT))

# --- Character Sprites --- #
player_sprite = pygame.image.load("assets/images/mila_normal_lit.png").convert_alpha() # tba
player_sprite = pygame.transform.scale(player_sprite, (700, 500))
mila_sprite = pygame.image.load("assets/images/mila_normal_lit.png").convert_alpha() # tba
mila_sprite = pygame.transform.scale(mila_sprite, (700, 500))
zombie = pygame.image.load("assets/images/zombie_jaw.png").convert_alpha()
zombie = pygame.transform.scale(zombie, (300, 300))

# source: https://www.reddit.com/r/aseprite/comments/v8wq1u/made_a_character_for_my_game_project/, edited by Chelsea
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