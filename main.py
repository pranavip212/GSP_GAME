import pygame
from game_states import GameState
from titlePage import title_screen
from scene1 import play_intro
from fight_game import play_fight
from at_School_s2 import at_School
from scene_3 import play_intro

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

current_state = GameState.TITLE

running = True

while running:

    if current_state == GameState.TITLE:
        current_state = title_screen(screen, clock)

    elif current_state == GameState.INTRO:
        current_state = play_intro(screen, clock)

    elif current_state == GameState.FIGHT:
        current_state = play_fight(screen, clock)

    elif current_state == GameState.GAME:
        current_state = at_School(screen, clock)

    elif current_state == GameState.SCENE3:
        current_state = play_intro(screen, clock)

    elif current_state == GameState.QUIT:
        running = False

pygame.quit()