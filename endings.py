import pygame
from constants import *

def play_ending(screen, clock, choice, outcome):
    main_font = pygame.freetype.SysFont("consolas", 70, bold=True)
    sub_font = pygame.freetype.SysFont("consolas", 28, bold=False)
    button_font = pygame.freetype.SysFont("consolas", 30, bold=True)

    fade_alpha = 255
    quit_button = pygame.Rect((344, 354, 90, 50))

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Choice Event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(event.pos):
                    quit()

        if outcome == "good":
            main_font.render_to(screen, (185, 100), "GOOD ENDING", WHITE)
            if choice == "talk":
                sub_font.render_to(screen, (280, 180), "You saved Mila.", WHITE)
            elif choice == "fight":
                sub_font.render_to(screen, (217, 180), "You fought Mila and won.", WHITE)

        elif outcome == "bad":
            main_font.render_to(screen, (205, 100), "BAD ENDING", WHITE)
            if choice == "talk":
                sub_font.render_to(screen, (259, 180), "Mila attacked you.", WHITE)
            elif choice == "fight":
                sub_font.render_to(screen, (240, 180), "Mila overpowered you.", WHITE)

        pygame.draw.rect(screen, BLACK, quit_button)
        if quit_button.collidepoint(pygame.mouse.get_pos()):
            button_font.render_to(screen, (355, 370), "QUIT", RED)
        else:
            button_font.render_to(screen, (355, 370), "QUIT", WHITE)

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        fade_alpha -= 2

        pygame.display.flip()