import pygame
from game_states import GameState
from title_page import title_screen

from fight_game import play_fight
from scene_1 import play_intro_s1
from scene_2 import play_intro_s2
from scene_3 import play_intro_s3

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

current_state = GameState.TITLE

running = True

while running:

    if current_state == GameState.TITLE:
        current_state = title_screen(screen, clock)

    elif current_state == GameState.INTRO:
        current_state = play_intro_s1(screen, clock)

    elif current_state == GameState.FIGHT:
        current_state = play_fight(screen, clock)

    elif current_state == GameState.GAME:
        current_state = play_intro_s2(screen, clock)

    elif current_state == GameState.SCENE3:
        current_state = play_intro_s3(screen, clock)

    elif current_state == GameState.QUIT:
        running = False

pygame.quit()