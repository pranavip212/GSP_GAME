import pygame
from constants import *
from game_states import GameState
from ui import DialogueBox
from images import *


def play_follow_mila(screen, clock):
    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    dialogue_lines = [
        [("Conflicted, you decide to follow Mila.", WHITE)],
        [("She shows the slightest smile, before ushering you to follow her into the maze.", WHITE)],
        [("Suddenly, Mila starts to limp...", WHITE)],
        [("She falls onto her knees, writhing in pain...", WHITE)]]

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not dialogue_box.finished:
                        dialogue_box.visible_characters = len(
                            dialogue_box.text_segments)

                    else:
                        current_line += 1
                        if current_line < len(dialogue_lines):
                            dialogue_box.set_text(
                                dialogue_lines[current_line])

                        else:
                            return GameState.GAME

        # visuals
        screen.blit(maze, (0, 0))
        screen.blit(pygame.transform.scale(mila_normal_dark, (195, 520)), (520, 120))

        if current_line >= 1:
            screen.blit(pygame.transform.scale(mila_happy_dark, (195, 520)), (520, 120))

        if current_line >= 2:
            screen.blit(maze_above, (0, 0)) # temp; free-roam should be here instead

        # update gui
        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()

def play_run_away(screen, clock):
    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    dialogue_lines = [
        [("Conflicted, you think back to this morning...", WHITE)],
        [("You remember the bloody breakfast Mila made you.", WHITE)],
        [("Looking at her, her cold, empty eyes, you make your decision:", WHITE)],
        [("Yep, not happening!", WHITE)],
        [("You turn around and just book it!", WHITE)],
        [("You reach a dead end and you see her coming closer.", WHITE)],
        [("Suddenly, Mila starts to limp...", WHITE)],
        [("She falls onto her knees, writhing in pain...", WHITE)]]

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not dialogue_box.finished:
                        dialogue_box.visible_characters = len(
                            dialogue_box.text_segments)

                    else:
                        current_line += 1
                        if current_line < len(dialogue_lines):
                            dialogue_box.set_text(
                                dialogue_lines[current_line])

                        else:
                            return GameState.GAME

        # visuals
        screen.blit(maze, (0, 0))
        screen.blit(pygame.transform.scale(mila_normal_dark, (195, 520)), (520, 120))

        if current_line >= 2:
            screen.blit(maze_above, (0, 0)) # temp; free-roam should be here instead

        # update gui
        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()