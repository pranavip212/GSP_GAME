import pygame
from constants import *
from ui import DialogueBox
from images import *


def play_transformation_s4(screen, clock):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = [
        [("Suddenly, Mila starts to limp and slow down...", WHITE)],
        [("She falls, clutching her head...", WHITE)],
        [("Her breath turns ragged, her eyes bloodshot...", WHITE)],
        [("Mila... are you okay?", WHITE)], # change colour to some colour once constant is made; player speaks
        [("So... hungry...", WHITE)], # change colour to some colour once constant is made; mila speaks
        [("She grabs your arm a little too tight.", WHITE)],
        [("Great, the only other survivor is a zombie.", WHITE)],
        [("Not to mention that she wants to eat you...", RED)],
        [("What will you do now?", WHITE)],]

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
                    play_final_s4(screen, clock, "follow_mila")
                    return
                elif run_button.collidepoint(event.pos):
                    play_final_s4(screen, clock, "run_away")
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
        screen.blit(maze, (0, 0))
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


def play_final_s4(screen, clock, choice):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = []

    if choice == "follow_mila":
        dialogue_lines = [
            [("Conflicted, you agree to follow Mila.", WHITE)],
            [("She smiles slightly in response.", WHITE)],
            [("She ushers you to go into the maze with her.", WHITE)]]

    elif choice == "run_away":
        dialogue_lines = [
            [("Conflicted, you think back to this morning...", WHITE)],
            [("You remember the breakfast Mila made you.", WHITE)],
            [("Her eyes are cold and empty...", WHITE)],
            [("Yep, not happening!", WHITE)],
            [("You turn around and just book it!", WHITE)]]

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
        if choice == "follow_mila":
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (520, 120))

            if current_line >= 1:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_happy_dark, True, False), (195, 520)), (520, 120))

            if current_line >= 2:
                screen.blit(maze, (0, 0))
                screen.blit(pygame.transform.scale(mila_normal_dark, (90, 240)), (190, 210))

        elif choice == "run_away":
            screen.blit(maze, (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (520, 120))

            if current_line >= 1:
                screen.blit(breakfast_gray, (0, 0))

            if current_line >= 2:
                screen.blit(maze, (0, 0))
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_pensive_dark, True, False), (195, 520)), (520, 120))

            if current_line >= 3:
                screen.blit(maze, (0, 0))
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (520, 120))

            if current_line >= 4:
                screen.blit(pygame.transform.flip(maze, True, False), (0, 0))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()

def play_final_talk_s4():
    pass


def play_final_fight_s4():
    pass
