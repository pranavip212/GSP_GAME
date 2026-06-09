import sys
import math
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



    # MAIN LOOP


    running = True

    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # PLAYER MOVEMENT


        keys = pygame.key.get_pressed()

        old_x = player.x
        old_y = player.y

        if keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        if keys[pygame.K_UP]:
            player.y -= player_speed

        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # Wall collision = lose
        for wall in walls:
            if player.colliderect(wall):
                game_over()


        # ZOMBIES


        for zombie in zombies:

            zombie["rect"].x += zombie["dir"] * 2

            if zombie["rect"].x < 250:
                zombie["dir"] = 1

            if zombie["rect"].x > 500:
                zombie["dir"] = -1

            if player.colliderect(zombie["rect"]):
                game_over()


        # FOLLOW MODE


        if mode == "follow_mode":

            distance = math.hypot(
                player.centerx - mila.centerx,
                player.centery - mila.centery
            )

            if distance > 80:
                move_towards(
                    mila,
                    player.center,
                    mila_speed
                )

        # =====================
        # RUN MODE
        # =====================

        if mode == "run_mode":

            move_towards(
                mila,
                player.center,
                chase_speed
            )

            if player.colliderect(mila):
                game_over()


        # TARGET


        if player.colliderect(target):
            play_intro_s4(screen, clock)


        # DRAW

        maze_screen.fill((20, 20, 20))

        for wall in walls:
            pygame.draw.rect(maze_screen, (80, 80, 80), wall)

        maze_screen.blit(pygame.transform.scale(target_sprite, (50, 50)), target)

        for zombie in zombies:
            maze_screen.blit(pygame.transform.scale(zombie_sprite, (50, 50)), zombie["rect"])

        maze_screen.blit(pygame.transform.scale(player_sprite, (50, 50)), player)
        maze_screen.blit(pygame.transform.scale(mila_sprite, (50, 50)), mila)

        pygame.display.flip()

    pygame.quit()