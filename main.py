"""import pygame
# setup

pygame.init()
screen_width = 1100
screen_length = 800

screen = pygame.display.set_mode((screen_width, screen_length ))
pygame.display.set_caption("Zombie PYOAG Game")
clock = pygame.time.Clock()

pygame.font.init()
font_1 = pygame.font.SysFont('monospace', 25, bold=False)
running = True

while running:
    # A. Check for Events (keyboard/mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # B. Update Game Logic (move characters, check collisions)

        # C. Drawing
        screen.fill((0, 0, 0))  # Clear screen with black
        # Add your drawing code here (e.g., pygame.draw.rect)

        pygame.display.update()  # Refresh the screen
        clock.tick(60)  # Limits the game to 60 frames per second
"""