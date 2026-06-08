print('fight scene loaded ')

import pygame
import random
import time
from constants import *
from at_School_s2 import at_School
from game_states import GameState

# =====================================
# COLORS
# =====================================

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 40, 40)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
DARK_GRAY = (40, 40, 40)
BLUE = (50, 120, 255)
ZOMBIE_GREEN = (60, 120, 80)
SKIN = (241, 194, 125)

# =====================================
# FONTS
# =====================================
pygame.font.init()

# =====================================
# SETTINGS
# =====================================

BAR_MAX = 100
START_BAR = 50

DRAIN_SPEED = 20
REFILL_AMOUNT = 5

FIGHT_DURATION = 10


def play_fight(screen, clock):
    print('fight scene started')

    shake = 0

    bedroom = pygame.image.load("assets/images/bedroom.png").convert()
    bedroom = pygame.transform.scale(bedroom, (WIDTH, HEIGHT))

    zombie = pygame.image.load("assets/images/zombie_jaw.png").convert_alpha()
    zombie = pygame.transform.scale(zombie, (300, 300))

    title_font = pygame.font.SysFont("consolas", 48)
    main_font = pygame.font.SysFont("consolas", 30)
    big_font = pygame.font.SysFont("consolas", 56)

    current_state = "intro"

    bar_value = START_BAR
    timer = FIGHT_DURATION

    dialogue_text = "A zombie attacks you! PRESS SPACE!"

    # =====================================
    # BLOOD
    # =====================================

    def draw_blood():

        for _ in range(10):

            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

            size = random.randint(2, 7)

            pygame.draw.circle(
                screen,
                (180, 0, 0),
                (x, y),
                size
            )

    # =====================================
    # MAIN LOOP
    # =====================================

    running = True

    while running:

        dt = clock.tick(60) / 1000

        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                #intor start
                if current_state == "intro":
                        current_state = "fight"
                        dialogue_text = "SPAM SPACE TO SURVIVE!"

                    #fight
                elif current_state == "fight":
                        bar_value += REFILL_AMOUNT
                        shake = 10

                        if bar_value > BAR_MAX:
                            bar_value = BAR_MAX

                elif current_state == "win":
                        at_School(screen, clock)

                elif current_state == "lose":
                        return GameState.INTRO


        # UPDATE

        if current_state == "fight":

            bar_value -= DRAIN_SPEED * dt

            timer -= dt

            if bar_value <= 0:
                bar_value = 0
                current_state = "lose"
                dialogue_text = "THE ZOMBIE OVERPOWERED YOU...PRESS SPACE"

            if timer <= 0:
                timer = 0
                current_state = "win"
                dialogue_text = "YOU SURVIVED! PRESS SPACE TO CONTINUE"

        # SHAKE AFFECT

        offset_x = 0
        offset_y = 0

        if shake > 0:
            offset_x = random.randint(-shake, shake)
            offset_y = random.randint(-shake, shake)

            shake -= 1

        #DRAW
        screen.blit(bedroom, (offset_x, offset_y))
        screen.blit(zombie, (525 + offset_x, 75 + offset_y))


        if current_state == "fight":
            draw_blood()

        # TITLE
        title = title_font.render(
            "ZOMBIE FIGHT",
            True,
            WHITE
        )

        screen.blit(title, (260, 40))

        # TIMER
        timer_text = main_font.render(f"TIME: {timer:.1f}", True, WHITE)
        screen.blit(timer_text, (360, 120))

        # BAR BG
        pygame.draw.rect(screen, DARK_GRAY, (150, 250, 500, 50))

        # BAR COLOR
        if bar_value > 60:
            color = GREEN
        elif bar_value > 30:
            color = YELLOW
        else:
            color = RED

        # BAR
        pygame.draw.rect(
            screen,
            color,
            (150, 250, int((bar_value / BAR_MAX) * 500), 50)
        )

        pygame.draw.rect(screen, WHITE, (150, 250, 500, 50), 3)

        # WIN/LOSE TEXT
        if current_state == "win":
            text = big_font.render("YOU SURVIVED!", True, GREEN)
            screen.blit(text, (210, 330))

        if current_state == "lose":
            text = big_font.render("THE ZOMBIE KILLED YOU", True, RED)
            screen.blit(text, (50, 330))


        # DIALOGUE

        pygame.draw.rect(screen, BLACK, (50, 390, 600, 80))
        pygame.draw.rect(screen, WHITE, (50, 390, 600, 80), 3)

        text_surface = main_font.render(dialogue_text, True, WHITE)
        screen.blit(text_surface, (70, 420))

        pygame.display.flip()