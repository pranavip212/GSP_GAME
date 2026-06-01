import pygame
from constants import *
from game_states import GameState
from chase_s3 import play_follow_mila
from chase_s3 import play_run_away
from ui import DialogueBox


def play_maze_game(screen, clock):
    hallway_lit = pygame.image.load('assets/images/hallway_lit.png').convert()
    hallway_lit = pygame.transform.scale(hallway_lit, (WIDTH, HEIGHT))
    hallway_dark = pygame.image.load('assets/images/hallway_dark.png').convert()
    hallway_dark = pygame.transform.scale(hallway_dark, (WIDTH, HEIGHT))
    maze = pygame.image.load('assets/images/maze.png').convert()
    maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))
    mila_normal_lit = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_normal_lit = pygame.transform.scale(mila_normal_lit, (750, 550))
    mila_normal_dark = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_normal_dark = pygame.transform.scale(mila_normal_dark, (750, 550))

    fade_alpha = 255
    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    dialogue_lines = [
        [("Following the scream, you both wander the halls.", WHITE)],
        [("Suddenly, the lights go out and you feel the ground shift...", WHITE)],
        [("You see the hallways twist and shift into a dark maze. ", WHITE)],
        [("Mila grabs your wrist and whispers to you:", WHITE)],
        [("We have to go. Now.", RED)], # change colour here
        [("You have to make a quick decision.", WHITE)],
        [("Do you trust Mila?", WHITE)]
    ]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    # choices
    show_choices = False

    # check runtime
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not dialogue_box.finished:
                        dialogue_box.visible_characters = len(
                            dialogue_box.text
                        )

                    else:
                        current_line += 1
                        if current_line < len(dialogue_lines):
                            dialogue_box.set_text(
                                dialogue_lines[current_line]
                            )

                        else:
                            if choose_follow:
                                play_follow_mila(screen, clock)
                            elif choose_run:
                                play_run_away(screen, clock)

        # visuals
        screen.blit(hallway_lit, (0, 0))
        screen.blit(mila_normal_lit, (10, 90))

        if current_line >= 1:
            screen.blit(hallway_dark, (0, 0))

        if current_line >= 2:
            screen.blit(maze, (0, 0))

        if current_line >= 3:
            screen.blit(mila_normal_dark, (10, 90))

        # fade effects
        if fade_alpha > 0:
            fade_surface = pygame.Surface((WIDTH, HEIGHT))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))
            fade_alpha -= 2

        # update gui
        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()