import pygame
import pygame.freetype
from constants import *

def play_ending(screen, clock, choice, outcome):
    main_font = pygame.freetype.SysFont("consolas", 70, bold=True)
    sub_font = pygame.freetype.SysFont("consolas", 28, bold=False)
    fade_alpha = 255

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)

        if outcome == "good":
            main_font.render_to(screen, (190, 100), "GOOD ENDING", WHITE)
            if choice == "talk":
                sub_font.render_to(screen, (290, 180), "You saved Mila.", WHITE)
            elif choice == "talk":
                pass

        if choice == "fight" and outcome == "good":
            pass
        elif choice == "fight" and outcome == "bad":
            pass

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        fade_alpha -= 2

        pygame.display.flip()