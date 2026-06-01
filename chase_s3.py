import pygame
from constants import *
from game_states import GameState
from ui import DialogueBox


def play_follow_mila(screen, clock):
    maze = pygame.image.load('assets/images/maze.png').convert()
    maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))
    maze_above = pygame.image.load('assets/images/maze_above.png').convert()
    maze_above = pygame.transform.scale(maze_above, (WIDTH, HEIGHT))
    mila_normal_dark = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_normal_dark = pygame.transform.scale(mila_normal_dark, (700, 500))
    mila_sprite_idle = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_sprite_idle = pygame.transform.scale(mila_sprite_idle, (700, 500))
    mila_sprite_walk_1 = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_sprite_walk_1 = pygame.transform.scale(mila_sprite_walk_1, (700, 500))
    mila_sprite_walk_2 = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_sprite_walk_2 = pygame.transform.scale(mila_sprite_walk_2, (700, 500))

    fade_alpha = 255
    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    dialogue_lines = [
        [("Conflicted, you decide to follow Mila.", WHITE)],
        [("She shows the slightest smile, before ushering you to follow her into the maze.", WHITE)],
        [("Suddenly, Mila starts to limp...", WHITE)],
        [("She falls onto her knees, writhing in pain...", WHITE)]
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
                            return GameState.GAME

        # visuals
        screen.blit(maze, (0, 0))
        screen.blit(mila_normal_dark, (-30, 50))

        if current_line >= 2:
            screen.blit(maze_above, (0, 0)) # temp; free-roam should be here instead

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

def play_run_away(screen, clock):
    maze = pygame.image.load('assets/images/maze.png').convert()
    maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))
    maze_above = pygame.image.load('assets/images/maze_above.png').convert()
    maze_above = pygame.transform.scale(maze_above, (WIDTH, HEIGHT))
    mila_normal_dark = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_normal_dark = pygame.transform.scale(mila_normal_dark, (700, 500))
    mila_sprite_idle = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_sprite_idle = pygame.transform.scale(mila_sprite_idle, (700, 500))
    mila_sprite_walk_1 = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_sprite_walk_1 = pygame.transform.scale(mila_sprite_walk_1, (700, 500))
    mila_sprite_walk_2 = pygame.image.load("assets/images/mila_standing_clear.png").convert_alpha()
    mila_sprite_walk_2 = pygame.transform.scale(mila_sprite_walk_2, (700, 500))

    fade_alpha = 255
    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    dialogue_lines = [
        [("Conflicted, you think back to this morning...", WHITE)],
        [("You remember the bloody breakfast Mila made you.", WHITE)],
        [("Looking at her, her cold, empty eyes, you make your decision:", WHITE)],
        [("Yep, not happening!", WHITE)],
        [("You turn around and just book it!", WHITE)],
        [("You reach a dead end and you see her coming closer.", WHITE)],
        [("Suddenly, Mila starts to limp...", WHITE)],
        [("She falls onto her knees, writhing in pain...", WHITE)]
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
                            return GameState.GAME

        # visuals
        screen.blit(maze, (0, 0))
        screen.blit(mila_normal_dark, (-30, 50))

        if current_line >= 2:
            screen.blit(maze_above, (0, 0)) # temp; free-roam should be here instead

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