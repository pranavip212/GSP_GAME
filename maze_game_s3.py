import pygame
from constants import *
from chase_s3 import play_follow_mila, play_run_away
from ui import DialogueBox
from images import *


def play_maze_game(screen, clock):

    fade_alpha = 255
    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    dialogue_lines = [
        [("Following the scream, you both wander the halls.", WHITE)],
        [("Suddenly, the lights go out and you feel the ground shift...", WHITE)],
        [("You see the hallways twist and shift into a dark maze. ", WHITE)],
        [("Mila grabs your wrist and whispers to you:", WHITE)],
        [("We have to go. Now.", (50, 120, 255))], # change colour to purple once constant is made
        [("You have to make a quick decision.", WHITE)],
        [("Do you trust Mila?", RED)]
    ]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    # choices, testing Button class
    show_choices = True

    class Button:
        def __init__(self, text, x, y, button_font, colour, hover_colour):
            self.text = text
            self.button_font = button_font
            self.colour = colour
            self.hover_colour = hover_colour
            self.rect = self.text.get_rect()

        def draw(self):
            action = False

            # check if mouse is over button
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    action = True

            screen.blit(self.text, (self.rect.x, self.rect.y))

            return action

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
                            play_follow_mila(screen, clock)

        # visuals
        screen.blit(hallway_lit, (0, 0))
        screen.blit(mila_normal_lit, (10, 90))

        if current_line >= 1:
            screen.blit(hallway_dark, (0, 0))

        if current_line >= 2:
            screen.blit(maze, (0, 0))

        if current_line >= 3:
            screen.blit(mila_normal_dark, (10, 90))

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