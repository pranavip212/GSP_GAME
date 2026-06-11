import time
import math
from ui import DialogueBox
from images import *
from scene_4 import play_intro_s4

def play_maze_game(mode):
    player_speed = 4
    mila_speed = 3
    player_start = (60, 60)
    mila_start = (30, 60)

    maze_width = 1000
    maze_height = 700
    maze_screen = pygame.display.set_mode((maze_width, maze_height))

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    instruction = [
        [("Sneak past the zombies and get to the exit! Don't alert them by touching the walls!", RED)],
        [("Run and get to the exit! Don't alert the zombies by touching the walls!", RED)]]
    dialogue_box = DialogueBox((10, 600, 720, 120))

    if mode == "follow_mode":
        dialogue_box.set_text(instruction[0])
    elif mode == "run_mode":
        dialogue_box.set_text(instruction[1])

    game_over_box = DialogueBox((205, 300, 610, 60))
    game_over_box.set_text([["You got caught! Press SPACE to retry!", RED]])

    # --- Game Objects --- #
    player = pygame.Rect(*player_start, 40, 40)
    mila = pygame.Rect(*mila_start, 40, 40)
    target = pygame.Rect(900, 600, 50, 50)

    walls = [
        pygame.Rect(0, 0, maze_width, 20),
        pygame.Rect(0, 0, 20, maze_height),
        pygame.Rect(0, maze_height - 20, maze_width, 20),
        pygame.Rect(maze_width - 20, 0, 20, maze_height),

        pygame.Rect(200, 0, 20, 500),
        pygame.Rect(400, 200, 20, 500),
        pygame.Rect(600, 0, 20, 450),
        pygame.Rect(800, 250, 20, 450)]

    zombies = [
        {"rect": pygame.Rect(300, 100, 40, 40), "dir": 1},
        {"rect": pygame.Rect(700, 400, 40, 40), "dir": -1}]

    def move_towards(rect, target_pos, speed):
        dx = target_pos[0] - rect.centerx
        dy = target_pos[1] - rect.centery

        dist = math.hypot(dx, dy)
        if dist > 0:
            dx /= dist
            dy /= dist
            rect.x += dx * speed
            rect.y += dy * speed

    def reset_game():
        player.topleft = player_start
        mila.topleft = mila_start
        return pygame.time.get_ticks()

    # --- Main Game Loop --- #
    game_over_state = False
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_over_state and event.key == pygame.K_SPACE:
                    start_ticks = reset_game()
                    game_over_state = False

        # --- GUI --- #
        maze_screen.blit(maze_ground, (0, 0))
        maze_screen.blit(pygame.transform.scale(player_sprite, (50, 50)), player)
        maze_screen.blit(pygame.transform.scale(mila_sprite, (60, 50)), mila)
        maze_screen.blit(pygame.transform.scale(target_sprite, (50, 50)), target)

        for wall in walls:
            pygame.draw.rect(maze_screen, (30, 30, 30), wall)
        for zombie_enemy in zombies:
            maze_screen.blit(pygame.transform.scale(zombie, (50, 50)), zombie_enemy["rect"])

        # --- Game State --- #
        if not game_over_state:

            # Player Movement
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                player.x -= player_speed
            if keys[pygame.K_RIGHT]:
                player.x += player_speed
            if keys[pygame.K_UP]:
                player.y -= player_speed
            if keys[pygame.K_DOWN]:
                player.y += player_speed

            # Lose Conditions
            for wall in walls:
                if player.colliderect(wall):
                    game_over_state = True

            for zombie_enemy in zombies:
                zombie_enemy["rect"].x += zombie_enemy["dir"] * 2

                if zombie_enemy["rect"].x < 250:
                    zombie_enemy["dir"] = 1
                if zombie_enemy["rect"].x > 500:
                    zombie_enemy["dir"] = -1

                if player.colliderect(zombie_enemy["rect"]):
                    game_over_state = True

            # Follow Mode
            if mode == "follow_mode":
                distance = math.hypot(player.centerx - mila.centerx, player.centery - mila.centery)
                if distance > 80:
                    move_towards(mila, player.center, mila_speed)

            # Run Mode
            if mode == "run_mode":
                move_towards(mila, player.center, mila_speed)
                elapsed_milliseconds = pygame.time.get_ticks() - start_ticks

                if elapsed_milliseconds > 2000 and player.colliderect(mila):
                    game_over_state = True

            # Win Condition
            if player.colliderect(target):
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                play_intro_s4(screen, clock)

        if not game_over_state:
            dialogue_box.update()
            dialogue_box.draw(maze_screen)

        elif game_over_state:
            game_over_box.update()
            game_over_box.draw(maze_screen)

        pygame.display.flip()