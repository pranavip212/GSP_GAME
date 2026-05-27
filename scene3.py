import pygame
from constants import *
from game_states import GameState
from ui import DialogueBox


def play_maze_game(screen, clock):
    # images
    bedroom = pygame.image.load('bedroom.png').convert()
    bedroom = pygame.transform.scale(bedroom, (WIDTH, HEIGHT))
    zombie = pygame.image.load("zombie_jaw.png").convert_alpha()
    zombie = pygame.transform.scale(zombie, (300, 300))

    # fade
    fade_alpha = 255

    dialogue_lines = [
        "Following the scream, you guys wander the halls.",
        "Out of nowhere, the lights go out and you feel the ground shift...",
        "The now setting sun illuminates the halls, and you see the hallways twist and shift into a dark maze.",
        "Mila grabs your wrist and whispers to you:",
        "'We have to go. Now.'"
        "Now, you have to make a quick decision.",
        "Do you trust Mila?"
    ]

    current_line = 0

    # create dialogue box
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    # choice buttons only appear later
    show_choices = False

    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    running = True

    while running:

        # limiting fps

        clock.tick(60)

        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
                running = False

            # key pressed
            if event.type == pygame.KEYDOWN:

                # SPACE advances dialogue
                if event.key == pygame.K_SPACE:

                    # if line still typing, finsh it
                    if not dialogue_box.finished:

                        dialogue_box.visible_characters = len(
                            dialogue_box.text
                        )

                    # otherwise go next line
                    else:

                        current_line += 1

                        # if dialogue remains
                        if current_line < len(dialogue_lines):

                            dialogue_box.set_text(
                                dialogue_lines[current_line]
                            )

                        # intro finished
                        else:
                            return GameState.GAME

        # draw bedroom
        screen.blit(bedroom, (0, 0))

        # reveal zombie w dialouge pacing
        if current_line >= 3:
            screen.blit(
                zombie,
                (250, 100)
            )

        # dark red horror overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))

        overlay.fill((20, 0, 0))

        overlay.set_alpha(40)

        screen.blit(overlay, (0, 0))
        # used chat for help with fade
        # fade from black at beginning
        if fade_alpha > 0:
            fade_surface = pygame.Surface((WIDTH, HEIGHT))

            fade_surface.fill(BLACK)

            fade_surface.set_alpha(fade_alpha)

            screen.blit(fade_surface, (0, 0))

            # slowly remove black screen
            fade_alpha -= 2

        # update typewriter effect
        dialogue_box.update()

        # draw dialogue
        dialogue_box.draw(screen)

        # update screen
        pygame.display.flip()