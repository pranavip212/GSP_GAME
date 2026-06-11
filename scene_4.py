import random
import pygame.freetype
from endings import *
from player_data import *
from ui import DialogueBox
from images import *


def play_intro(screen, clock):
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    dialogue_lines = [
        [("Suddenly, Mila starts to limp and slow down...", WHITE)],
        [("She falls, clutching her head...", WHITE)],
        [("Her breath turns ragged, her eyes bloodshot...", WHITE)],
        [("YOU: Mila... are you okay?", WHITE)],
        [("MILA: So... hungry...", PURPLE)],
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
                    play_transition(screen, clock, "talk")
                    return
                elif fight_button.collidepoint(event.pos):
                    play_transition(screen, clock, "fight")
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


def play_transition(screen, clock, choice):
    dialogue_lines = []

    if choice == "talk":
        dialogue_lines = [
            [("You hold up your hands defensively.", WHITE)],
            [("YOU: Mila, listen to me!", WHITE)],
            [("She freezes, her body trembling...", WHITE)],
            [("YOU: This isn't you!", WHITE)],
            [("YOU: You're stronger than this. I know you can fight it.", WHITE)],
            [("Her snarls fade, replaced by confusion.", WHITE)]]

    elif choice == "fight":
        dialogue_lines = [
            [("You hold up your hands defensively.", WHITE)],
            [("YOU: Don't make me do this, Mila!", WHITE)],
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
                            play_talk(screen, clock)
                        elif choice == "fight":
                            play_fight(screen, clock)

        # --- GUI --- #
        screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
        screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (400, 120))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()


def play_talk(screen, clock):
    dialogue_lines = []

    if trust >= 1:
        dialogue_lines = [
            [("Mila gasps, her eyes returning into normal.", WHITE)],
            [("MILA: I... I remember now.", PURPLE)],
            [("MILA: You're right. I'm still human...", PURPLE)],
            [("Her voice trembles as she collapses onto the floor, human once more.", WHITE)]]

    elif trust < 1:
        dialogue_lines = [
            [("Her eyes flicker for a split second...", WHITE)],
            [("..before sharpening again, full of rage.", RED)],
            [("MILA: I can't... fight it...", PURPLE)],
            [("She growls and lunges at you, her claws tearing through the air.", DARK_RED)]]

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
                            transition_good_ending(screen, clock, "talk")
                        elif trust < 1:
                            transition_bad_ending(screen, clock, "talk")

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
                screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (230, 610)), (340, 100))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()


def play_fight(screen, clock):
    dialogue_lines = []

    if has_knife:
        dialogue_lines = [
            [("You reach to your ankle and take the knife out, holding it in front of yourself.", WHITE)],
            [("With all of your strength, you knock Mila to the ground.", WHITE)],
            [("She lies there panting, and her eyes slowly fade back to normal.", WHITE)],
            [("MILA: It's... over...", PURPLE)]]

    elif not has_knife:
        dialogue_lines = [
            [("However, you misjudge her next move, and her claws rip into you.", RED)],
            [("Pain shoots through your body as you collapse to the ground.", RED)],
            [("Her snarls are the last thing you hear before you fade into darkness...", DARK_RED)]]

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
                            transition_good_ending(screen, clock, "fight")
                        elif not has_knife:
                            transition_bad_ending(screen, clock, "fight")

        # --- GUI --- #
        screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
        screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (195, 520)), (400, 120))

        if has_knife:
            if current_line >= 1:
                screen.blit(pygame.transform.flip(maze, True, False), (0, 0))

        elif not has_knife:
            screen.blit(pygame.transform.flip(maze, True, False), (0, 0))
            screen.blit(pygame.transform.scale(pygame.transform.flip(mila_silhouette, True, False), (230, 610)), (340, 100))

        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()


def transition_good_ending(screen, clock, choice):
    fade_alpha = 0

    running = True
    while running:
        clock.tick(60)

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 1
        if fade_alpha >= 50:
            if choice == "talk":
                play_ending(screen, clock, "talk", "good")
            elif choice == "fight":
                play_ending(screen, clock, "fight", "good")
            running = False

        pygame.display.flip()


def transition_bad_ending(screen, clock, choice):
    shake = 0
    scale = 0.2
    flash_alpha = 0
    fade_alpha = 0

    phase = "jumpscare"
    running = True
    while running:
        clock.tick(60)

        if phase == "jumpscare":
            scale += 0.1

            shake = min(20, shake + 1)
            offset_x = random.randint(-shake, shake)
            offset_y = random.randint(-shake, shake)
            screen.blit(pygame.transform.flip(maze, True, False), (offset_x, offset_y))

            zombie_hand_width = int(zombie_hand.get_width() * scale)
            zombie_hand_height = int(zombie_hand.get_height() * scale)
            zombie_hand_jumpscare = pygame.transform.scale(zombie_hand, (zombie_hand_width, zombie_hand_height))

            rect = zombie_hand_jumpscare.get_rect(center=((WIDTH // 2) + 70, (HEIGHT // 2) - 20))
            screen.blit(zombie_hand_jumpscare, rect)

            if scale >= 2.5:
                phase = "flash"

        elif phase == "flash":
            flash_surface = pygame.Surface((WIDTH, HEIGHT))
            flash_surface.fill((255,0,0))
            flash_surface.set_alpha(flash_alpha)
            screen.blit(flash_surface, (0, 0))
            flash_alpha += 25

            if flash_alpha >= 255:
                phase = "fade"

        elif phase == "fade":
            fade_surface = pygame.Surface((WIDTH, HEIGHT))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))

            fade_alpha += 1

            if fade_alpha >= 50:
                if choice == "talk":
                    play_ending(screen, clock, "talk", "bad")
                elif choice == "fight":
                    play_ending(screen, clock, "fight", "bad")
                running = False

        pygame.display.flip()