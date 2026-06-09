import sys
import math
import time
from images import *
from scene_4 import play_intro_s4

def play_maze_game(mode):
    maze_width = 1000
    maze_height = 700
    player_speed = 4
    mila_speed = 3
    chase_speed = 3.5

    maze_screen = pygame.display.set_mode((maze_width, maze_height))
    clock = pygame.time.Clock()

    # --- Game Objects --- #
    player = pygame.Rect(60, 60, 40, 40)
    mila = pygame.Rect(30, 60, 40, 40)
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

    def game_over():

        print("GAME OVER") # to be edited
        pygame.quit()
        sys.exit()


    def move_towards(rect, target_pos, speed):
        dx = target_pos[0] - rect.centerx
        dy = target_pos[1] - rect.centery

        dist = math.hypot(dx, dy)
        if dist > 0:
            dx /= dist
            dy /= dist
            rect.x += dx * speed
            rect.y += dy * speed

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
                game_over()

        for zombie_enemy in zombies:
            zombie_enemy["rect"].x += zombie_enemy["dir"] * 2

            if zombie_enemy["rect"].x < 250:
                zombie_enemy["dir"] = 1
            if zombie_enemy["rect"].x > 500:
                zombie_enemy["dir"] = -1
            if player.colliderect(zombie_enemy["rect"]):
                game_over()


        # Follow Mode
        if mode == "follow_mode":
            distance = math.hypot(player.centerx - mila.centerx, player.centery - mila.centery)

            if distance > 80:
                move_towards(mila, player.center, mila_speed)

        # Run Mode
        if mode == "run_mode":
            move_towards(mila, player.center, chase_speed)

            if player.colliderect(mila):
                game_over()


        # Win Condition
        if player.colliderect(target):
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            play_intro_s4(screen, clock)


        # --- GUI --- #
        maze_screen.fill((20, 20, 20))

        for wall in walls:
            pygame.draw.rect(maze_screen, (80, 80, 80), wall)

        maze_screen.blit(pygame.transform.scale(target_sprite, (50, 50)), target)

        for zombie_enemy in zombies:
            maze_screen.blit(pygame.transform.scale(zombie_sprite, (50, 50)), zombie_enemy["rect"])

        maze_screen.blit(pygame.transform.scale(player_sprite, (50, 50)), player)
        maze_screen.blit(pygame.transform.scale(mila_sprite, (50, 50)), mila)

        pygame.display.flip()