import pygame
import random
import sys
from constants import *
from game_states import GameState
from ui import DialogueBox

pygame.init()

# =====================================
# SCREEN
# =====================================

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Fight Scene")

clock = pygame.time.Clock()

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

title_font = pygame.font.SysFont("arial", 48)
main_font = pygame.font.SysFont("arial", 30)
big_font = pygame.font.SysFont("arial", 56)

# =====================================
# GAME SETTINGS
# =====================================

BAR_MAX = 100
START_BAR = 50

DRAIN_SPEED = 20
REFILL_AMOUNT = 5

FIGHT_DURATION = 10

# =====================================
# GAME STATES
# =====================================

class GameState:
    INTRO = "intro"
    FIGHT = "fight"
    WIN = "win"
    LOSE = "lose"

current_state = GameState.INTRO

# =====================================
# GAME VARIABLES
# =====================================

bar_value = START_BAR
timer = FIGHT_DURATION

# =====================================
# DIALOGUE BOX
# =====================================

class DialogueBox:

    def __init__(self):
        self.text = ""

    def show(self, text):
        self.text = text

    def draw(self):

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (50, 390, 800, 80)
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (50, 390, 800, 80),
            3
        )

        text_surface = main_font.render(
            self.text,
            True,
            WHITE
        )

        screen.blit(text_surface, (70, 420))

dialogue = DialogueBox()

dialogue.show("A zombie attacks you! PRESS SPACE!")

# =====================================
# RESTART GAME
# =====================================

def restart_game():

    global current_state
    global bar_value
    global timer

    current_state = GameState.INTRO

    bar_value = START_BAR
    timer = FIGHT_DURATION

    dialogue.show(
        "A zombie attacks you! PRESS SPACE!"
    )

# =====================================
# DRAW PLAYER
# =====================================

def draw_player():

    # Body
    pygame.draw.rect(screen, BLUE, (150, 170, 90, 150))

    # Head
    pygame.draw.rect(screen, SKIN, (165, 110, 60, 60))

    # Arms
    pygame.draw.rect(screen, BLUE, (120, 190, 30, 80))
    pygame.draw.rect(screen, BLUE, (240, 190, 30, 80))

    # Legs
    pygame.draw.rect(screen, BLUE, (165, 320, 25, 80))
    pygame.draw.rect(screen, BLUE, (205, 320, 25, 80))

# =====================================
# DRAW ZOMBIE
# =====================================

def draw_zombie():

    # Body
    pygame.draw.rect(
        screen,
        ZOMBIE_GREEN,
        (650, 150, 120, 180)
    )

    # Head
    pygame.draw.rect(
        screen,
        (80, 160, 100),
        (670, 90, 80, 80)
    )

    # Eyes
    pygame.draw.rect(screen, RED, (685, 115, 12, 12))
    pygame.draw.rect(screen, RED, (723, 115, 12, 12))

    # Mouth
    pygame.draw.rect(screen, BLACK, (695, 145, 30, 8))

    # Arms
    pygame.draw.rect(
        screen,
        ZOMBIE_GREEN,
        (620, 170, 30, 100)
    )

    pygame.draw.rect(
        screen,
        ZOMBIE_GREEN,
        (770, 170, 30, 100)
    )

    # Legs
    pygame.draw.rect(
        screen,
        ZOMBIE_GREEN,
        (675, 330, 30, 80)
    )

    pygame.draw.rect(
        screen,
        ZOMBIE_GREEN,
        (720, 330, 30, 80)
    )
# DRAW BLOOD EFFECT

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

# DRAW UI

def draw_ui():
    title = title_font.render(
        "ZOMBIE FIGHT",
        True,
        WHITE
    )

    screen.blit(title, (260, 40))

    timer_text = main_font.render(
        f"TIME: {timer:.1f}",
        True,
        WHITE
    )

    screen.blit(timer_text, (360, 120))


    pygame.draw.rect(
        screen,
        DARK_GRAY,
        (150, 250, 500, 50)
    )

    # Bar color
    if bar_value > 60:
        color = GREEN
    elif bar_value > 30:
        color = YELLOW
    else:
        color = RED

    # Filled bar
    pygame.draw.rect(
        screen,
        color,
        (
            150,
            250,
            int((bar_value / BAR_MAX) * 500),
            50
        )
    )

    # Border
    pygame.draw.rect(
        screen,
        WHITE,
        (150, 250, 500, 50),
        3
    )

    # Win message
    if current_state == GameState.WIN:
        text = big_font.render(
            "YOU SURVIVED!",
            True,
            GREEN
        )

        screen.blit(text, (210, 330))

    # Lose message
    if current_state == GameState.LOSE:
        text = big_font.render(
            "THE ZOMBIE KILLED YOU",
            True,
            RED
        )

        screen.blit(text, (50, 330))

    # Restart message
    if current_state in [GameState.WIN, GameState.LOSE]:
        restart = main_font.render(
            "PRESS SPACE TO RESTART",
            True,
            WHITE
        )

        screen.blit(restart, (250, 420))

    dialogue.draw()


# UPDATE GAME

def update(dt):

    global bar_value
    global timer
    global current_state

    if current_state != GameState.FIGHT:
        return
    # drain bar
    bar_value -= DRAIN_SPEED * dt
    # countdown
    timer -= dt
    # Lose
    if bar_value <= 0:

        bar_value = 0

        current_state = GameState.LOSE

        dialogue.show(
            "THE ZOMBIE OVERPOWERED YOU..."
        )

    # Win

    if timer <= 0:

        timer = 0

        current_state = GameState.WIN

        dialogue.show(
            "YOU SURVIVED THE ATTACK!"
        )


# MAIN LOOP

running = True

while running:
    dt = clock.tick(60) / 1000

    # EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if current_state == GameState.INTRO:

                    current_state = GameState.FIGHT

                    dialogue.show(
                        "SPAM SPACE TO SURVIVE!"
                    )

                elif current_state == GameState.FIGHT:




