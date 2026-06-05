import pygame
from constants import *
from game_states import GameState
from ui import DialogueBox
from images import *


def play_transition_s3(screen, clock, condition):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    if condition == "follow_mila":
        dialogue_lines = [
            [("Conflicted, you decide to follow Mila.", WHITE)],
            [("She smiles slightly in response.", WHITE)],
            [("She ushers you to go into the maze with her.", WHITE)]]

    elif condition == "run_away":
        dialogue_lines = [
            [("Conflicted, you think back to this morning...", WHITE)],
            [("You remember the bloody breakfast Mila made you.", WHITE)],
            [("Looking at her, her cold, empty eyes, you make your decision:", WHITE)],
            [("Yep, not happening!", WHITE)],
            [("You turn around and just book it!", WHITE)],
            [("Run!!!", WHITE)]]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Dialogue Event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_line += 1

                    if current_line < len(dialogue_lines):
                        dialogue_box.set_text(dialogue_lines[current_line])
                    else:
                        print("transition to maze game here")

        # --- GUI --- #
        if condition == "follow_mila":
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(mila_normal_dark, (195, 520)), (520, 120))

            if current_line >= 1:
                screen.blit(pygame.transform.scale(mila_happy_dark, (195, 520)), (520, 120))

            if current_line >= 2:
                screen.blit(maze, (0, 0))
                screen.blit(pygame.transform.scale(mila_normal_dark, (90, 240)), (190, 210))

        elif condition == "run_away":
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(mila_pensive_dark, (195, 520)), (520, 120))

            if current_line >= 1:
                screen.blit(pygame.transform.scale(mila_happy_dark, (195, 520)), (520, 120))

            if current_line >= 2:
                screen.blit(maze, (0, 0))
                screen.blit(pygame.transform.scale(mila_normal_dark, (90, 240)), (190, 210))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()