import pygame
from constants import *
from player_data import *
from ui import DialogueBox
from images import *


def play_intro_s4(screen, clock):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = [
        [("Suddenly, Mila starts to limp and slow down...", WHITE)],
        [("She falls, clutching her head...", WHITE)],
        [("Her breath turns ragged, her eyes bloodshot...", WHITE)],
        [('"Mila... are you okay?"', WHITE)], # change colour; player speaks
        [('"So... hungry..."', PURPLE)],
        [("She grabs your arm a little too tight.", WHITE)],
        [("Great, the only other survivor is a zombie, too.", WHITE)],
        [("Not to mention that she wants to eat you...", RED)],
        [("What will you do now?", WHITE)],]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    show_choice = False
    talk_button = pygame.Rect((40, 310, 340, 60))
    fight_button = pygame.Rect((40, 380, 210, 60))

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Choice Event
            if show_choice and event.type == pygame.MOUSEBUTTONDOWN:
                if talk_button.collidepoint(event.pos):
                    play_final_transition_s4(screen, clock, "talk")
                    return
                elif fight_button.collidepoint(event.pos):
                    play_final_transition_s4(screen, clock, "fight")
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
        screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
        screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (70, 190)), (490, 230))

        if current_line >= 1:
            screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (100, 270)), (470, 210))

        if current_line >= 5:
            screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (400, 120))

        if current_line >= 8:
            screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (520, 120))

        if show_choice:
            pygame.draw.rect(screen, BLACK, talk_button)
            pygame.draw.rect(screen, BLACK, fight_button)
            pygame.draw.rect(screen, (180, 30, 30), talk_button, 3)
            pygame.draw.rect(screen, (180, 30, 30), fight_button, 3)

            if talk_button.collidepoint(pygame.mouse.get_pos()):
                font.render_to(screen, (61, 330), "Talk her out of it.", RED)
            else:
                font.render_to(screen, (61, 330), "Talk her out of it.", WHITE)

            if fight_button.collidepoint(pygame.mouse.get_pos()):
                font.render_to(screen, (61, 400), "Fight her!", RED)
            else:
                font.render_to(screen, (61, 400), "Fight her!", WHITE)

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()


def play_final_transition_s4(screen, clock, choice):
    dialogue_lines = []

    if choice == "talk":
        dialogue_lines = [
            [("You hold up your hands defensively.", WHITE)],
            [('"Mila, listen to me!"', WHITE)], # change colour, player speaks
            [("She freezes, her body trembling...", WHITE)],
            [('"This is not you!"', WHITE)], # change colour, player speaks
            [('"You are stronger than this. I know you can fight it."', WHITE)], # change colour, player speaks
            [("Her snarls fade, replaced by confusion.", WHITE)]]

    elif choice == "fight":
        dialogue_lines = [
            [("You hold up your hands defensively.", WHITE)],
            [('"Do not make me do this, Mila!"', WHITE)],
            [("Despite your warning, she only growls.", WHITE)],
            [("She retaliates by attacking you while you duck and dodge!", WHITE)]]

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
                        if choice == "talk":
                            play_final_talk_s4(screen, clock)
                        elif choice == "fight":
                            play_final_fight_s4(screen, clock)

        # --- GUI --- #
        screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
        screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (400, 120))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()

def play_final_talk_s4(screen, clock):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = []

    if trust >= 1:
        dialogue_lines = [
            [("Mila gasps, her eyes returning into normal.", WHITE)],
            [('"I... I remember now."', PURPLE)],
            [('"You are right. I am still human..."', PURPLE)],
            [("Her voice trembles as she collapses onto the floor, human once more.", WHITE)]]

    elif trust < 1:
        dialogue_lines = [
            [("Her eyes flicker for a split second...", WHITE)],
            [("..before sharpening again, full of rage.", WHITE)],
            [('"I cannot... fight it..."', PURPLE)],
            [("She growls and lunges at you, her claws tearing through the air.", WHITE)]]

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
                        if trust >= 1:
                            print("good ending")
                            # play_ending(screen, clock, "talk", "good")
                        elif trust < 1:
                            print("bad ending")
                            # play_ending(screen, clock, "talk", "bad")

        # --- GUI --- #
        screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
        screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (400, 120))

        if trust >= 1:
            if current_line >= 1:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_pensive_dark, True, False), (195, 520)), (400, 120))
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_tears_dark, True, False), (195, 520)), (400, 120))

            if current_line >= 2:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (400, 120))
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_tears_dark, True, False), (195, 520)), (400, 120))

            if current_line >= 3:
                screen.blit(pygame.transform.flip(maze, True, False), (0, 0))

        elif trust < 1:
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_tears_dark, True, False), (195, 520)), (400, 120))

            if current_line >= 1:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (400, 120))

            if current_line >= 3:
                screen.blit(pygame.transform.flip(maze, True, False), (0, 0))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()


def play_final_fight_s4(screen, clock):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = []

    if has_knife:
        dialogue_lines = [
            [("You reach to your ankle and take the knife out, holding it in front of yourself.", WHITE)],
            [("With all your energy, you knock Mila to the ground.", WHITE)],
            [("She lies there panting, and her eyes slowly fade back to normal.", WHITE)],
            [('"It is... over..."', PURPLE)]]

    elif not has_knife:
        dialogue_lines = [
            [("However, you misjudge her next move, and her claws rip into you.", WHITE)],
            [("Pain shoots through your body as you collapse to the ground.", WHITE)],
            [("Her snarls are the last thing you hear before you fade into darkness...", WHITE)]]

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
                        if has_knife:
                            print("good ending")
                            # play_ending(screen, clock, "fight", "good")
                        elif not has_knife:
                            print("bad ending")
                            # play_ending(screen, clock, "fight", "bad")

        # --- GUI --- #
        screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
        screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (400, 120))

        if trust >= 1:
            if current_line >= 1:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_pensive_dark, True, False), (195, 520)), (400, 120))
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_tears_dark, True, False), (195, 520)), (400, 120))

            if current_line >= 2:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_normal_dark, True, False), (195, 520)), (400, 120))
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_tears_dark, True, False), (195, 520)), (400, 120))

            if current_line >= 3:
                screen.blit(pygame.transform.flip(maze, True, False), (0, 0))

        elif trust < 1:
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_tears_dark, True, False), (195, 520)), (400, 120))

            if current_line >= 1:
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (400, 120))

            if current_line >= 3:
                screen.blit(pygame.transform.flip(maze, True, False), (0, 0))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()
