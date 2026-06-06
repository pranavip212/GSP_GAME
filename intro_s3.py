import pygame
from constants import *
from transition_s3 import play_transition_s3
from ui import DialogueBox
from images import *


def play_intro_s3(screen, clock):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = [
        [("Curious, you both wander the halls.", WHITE)],
        [("Suddenly, the lights go out...", WHITE)],
        [("You feel the ground move...", WHITE)],
        [("The hallways twist and shift into a dark maze.", WHITE)],
        [("Mila abruptly grabs your wrist:", WHITE)],
        [("We have to go. Now.", (50, 120, 255))], # change colour to purple once constant is made; maybe indicate speaker (?)
        [("You have to make a quick decision.", WHITE)],
        [("Do you trust Mila?", RED)]]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    show_choice = False
    follow_button = pygame.Rect((40, 310, 220, 60))
    run_button = pygame.Rect((40, 380, 220, 60))

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Choice Event
            if show_choice and event.type == pygame.MOUSEBUTTONDOWN:
                if follow_button.collidepoint(event.pos):
                    play_transition_s3(screen, clock, "follow_mila")
                    return
                elif run_button.collidepoint(event.pos):
                    play_transition_s3(screen, clock, "run_away")
                    return

            # Dialogue Event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not show_choice:
                    current_line += 1

                    if current_line < len(dialogue_lines):
                        dialogue_box.set_text(dialogue_lines[current_line])
                    else:
                        show_choice = True


        # --- GUI --- #
        screen.blit(hallway_lit, (0, 0))
        screen.blit(pygame.transform.scale(mila_normal_lit, (195, 520)), (520, 120))

        if current_line >= 1:
            screen.blit(hallway_dark, (0, 0))

        if current_line >= 3:
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(mila_normal_dark, (195, 520)), (520, 120))

        if current_line >= 4:
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (250, 640)), (485, 90))

        if current_line >= 5:
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_pensive_dark, True, False), (250, 640)), (485, 90))

        if current_line >= 6:
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (520, 120))

        if show_choice:
            pygame.draw.rect(screen, BLACK, follow_button)
            pygame.draw.rect(screen, BLACK, run_button)
            pygame.draw.rect(screen, (180, 30, 30), follow_button, 3)
            pygame.draw.rect(screen, (180, 30, 30), run_button, 3)

            if follow_button.collidepoint(pygame.mouse.get_pos()):
                font.render_to(screen, (61, 330), "Follow her.", RED)
            else:
                font.render_to(screen, (61, 330), "Follow her.", WHITE)

            if run_button.collidepoint(pygame.mouse.get_pos()):
                font.render_to(screen, (61, 400), "Run away!", RED)
            else:
                font.render_to(screen, (61, 400), "Run away!", WHITE)

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()