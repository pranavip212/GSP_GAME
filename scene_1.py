import pygame.freetype
from images import *
from fight_game import play_fight
from ui import DialogueBox


def play_intro_s1(screen, clock):

    # fade
    fade_alpha = 255

    dialogue_lines = [

        [("Press space to begin/continue.", WHITE)],

        [("You were having the best nap of your life...", WHITE)],

        [("Something feels cold on your face.", WHITE)],

        [("...wait.", RED)],

        [("This isn't YOUR drool.", RED)],

        [("A zombie is hovering inches above you.", WHITE)],

        [("Before you can react...", RED)]

    ]

    current_line = 0


    # create dialogue box
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])
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

                    current_line += 1

                    # automatically advance to next line
                    if current_line < len(dialogue_lines):
                        dialogue_box.set_text(dialogue_lines[current_line])

                    # otherwise play next scene
                    else:
                        play_fight(screen, clock)

        # draw bedroom
        screen.blit(bedroom, (0, 0))

        # reveal zombie w dialogue pacing
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