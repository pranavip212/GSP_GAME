import pygame
import sys
import math

pygame.init()

# =========================
# SETTINGS
# =========================

WIDTH = 1000
HEIGHT = 700

FOLLOW_MODE = True      # Set by previous choice
RUN_MODE = not FOLLOW_MODE

PLAYER_SPEED = 4
MILA_SPEED = 3
CHASE_SPEED = 3.5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Fight Piece")

clock = pygame.time.Clock()

# =========================
# LOAD ASSETS
# =========================

maze_img = pygame.image.load("assets/images/maze.png").convert()

player_img = pygame.image.load("assets/images/player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (40, 40))

mila_img = pygame.image.load("assets/images/mila_happy_lit.png").convert_alpha()
mila_img = pygame.transform.scale(mila_img, (40, 40))

zombie_img = pygame.image.load("assets/images/zombie_jaw.png").convert_alpha()
zombie_img = pygame.transform.scale(zombie_img, (40, 40))

target_img = pygame.image.load("assets/images/target.png").convert_alpha()
target_img = pygame.transform.scale(target_img, (50, 50))

# =========================
# OBJECTS
# =========================

player = pygame.Rect(60, 60, 40, 40)

mila = pygame.Rect(30, 60, 40, 40)

target = pygame.Rect(900, 600, 50, 50)

# Maze walls
walls = [
    pygame.Rect(0, 0, WIDTH, 20),
    pygame.Rect(0, 0, 20, HEIGHT),
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    pygame.Rect(WIDTH - 20, 0, 20, HEIGHT),

    pygame.Rect(200, 0, 20, 500),
    pygame.Rect(400, 200, 20, 500),
    pygame.Rect(600, 0, 20, 450),
    pygame.Rect(800, 250, 20, 450),
]

# Zombies
zombies = [
    {
        "rect": pygame.Rect(300, 100, 40, 40),
        "dir": 1
    },
    {
        "rect": pygame.Rect(700, 400, 40, 40),
        "dir": -1
    }
]

# =========================
# FUNCTIONS
# =========================

def game_over():
    print("GAME OVER")
    pygame.quit()
    sys.exit()


def transformation():
    print("TRANSFORMATION")
    pygame.quit()
    sys.exit()


def move_towards(rect, target_pos, speed):
    dx = target_pos[0] - rect.centerx
    dy = target_pos[1] - rect.centery

    distance = math.hypot(dx, dy)

    if distance > 0:
        dx /= distance
        dy /= distance

        rect.x += dx * speed
        rect.y += dy * speed


# =========================
# MAIN LOOP
# =========================

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # =====================
    # PLAYER MOVEMENT
    # =====================

    keys = pygame.key.get_pressed()

    old_x = player.x
    old_y = player.y

    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED

    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED

    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Wall collision = lose
    for wall in walls:
        if player.colliderect(wall):
            game_over()

    # =====================
    # ZOMBIES
    # =====================

    for zombie in zombies:

        zombie["rect"].x += zombie["dir"] * 2

        if zombie["rect"].x < 250:
            zombie["dir"] = 1

        if zombie["rect"].x > 500:
            zombie["dir"] = -1

        if player.colliderect(zombie["rect"]):
            game_over()

    # =====================
    # FOLLOW MODE
    # =====================

    if FOLLOW_MODE:

        distance = math.hypot(
            player.centerx - mila.centerx,
            player.centery - mila.centery
        )

        if distance > 80:
            move_towards(
                mila,
                player.center,
                MILA_SPEED
            )

    # =====================
    # RUN MODE
    # =====================

    if RUN_MODE:

        move_towards(
            mila,
            player.center,
            CHASE_SPEED
        )

        if player.colliderect(mila):
            game_over()

    # =====================
    # TARGET
    # =====================

    if player.colliderect(target):
        transformation()

    # =====================
    # DRAW
    # =====================

    screen.fill((20, 20, 20))

    screen.blit(maze_img, (0, 0))

    for wall in walls:
        pygame.draw.rect(screen, (80, 80, 80), wall)

    screen.blit(target_img, target)

    for zombie in zombies:
        screen.blit(zombie_img, zombie["rect"])

    screen.blit(player_img, player)
    screen.blit(mila_img, mila)

    pygame.display.flip()

pygame.quit()