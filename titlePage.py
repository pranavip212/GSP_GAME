import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum
from constants import *
from scene1 import play_intro
from game_states import GameState
pygame.init()


# ---------------- TEXT FUNCTION ----------------
def create_surface_with_text(text, font_size, text_rgb):
    font = pygame.freetype.SysFont("consolas", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()


# ---------------- BUTTON CLASS ----------------
class UIElement(Sprite):
    def __init__(
        self,
        center_position,
        text,
        font_size,
        text_rgb,
        action=None,
    ):

        self.mouse_over = False
        self.action = action

        # default button image
        default_image = create_surface_with_text(
            text=text,
            font_size=font_size,
            text_rgb=text_rgb,
        )


        highlighted_image = create_surface_with_text(
            text=text,
            font_size=int(font_size * 1.2),
            text_rgb=RED,
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True

            if mouse_up:
                return self.action

        else:
            self.mouse_over = False

        return None

    def draw(self, surface):
        surface.blit(self.image, self.rect)



# ---------------- MAIN ----------------
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LAST BELL")

    clock = pygame.time.Clock()

    game_state = GameState.TITLE

    while True:

        if game_state == GameState.TITLE:
            game_state = title_screen(screen, clock)

        elif game_state == GameState.INTRO:
            game_state = play_intro(screen, clock)

        elif game_state == GameState.GAME:
            game_state = play_level(screen, clock)

        elif game_state == GameState.QUIT:
            pygame.quit()
            return


# ---------------- TITLE SCREEN ----------------
def title_screen(screen, clock):

    start_btn = UIElement(
        center_position=(WIDTH // 2, 380),
        font_size=40,
        text_rgb=WHITE,
        text="START",
        action=GameState.INTRO,
    )

    quit_btn = UIElement(
        center_position=(WIDTH // 2, 470),
        font_size=40,
        text_rgb=WHITE,
        text="QUIT",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    # title text
    title_font = pygame.freetype.SysFont("consolas", 72, bold=True)

    subtitle_font = pygame.freetype.SysFont("consolas", 24)

    while True:

        mouse_up = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_up = True

        # background
        screen.fill(BLACK)

        # red fog effect
        pygame.draw.circle(screen, DARK_RED, (400, 200), 250)

        # title
        title_font.render_to(
            screen,
            (190, 120),
            "LAST BELL",
            RED
        )

        # subtitle
        subtitle_font.render_to(
            screen,
            (240, 210),
            "A Zombie Visual Horror Game",
            WHITE
        )

        # buttons
        for button in buttons:

            ui_action = button.update(
                pygame.mouse.get_pos(),
                mouse_up
            )

            if ui_action is not None:
                return ui_action

            button.draw(screen)

        pygame.display.flip()
        clock.tick(60)


# ---------------- GAME SCREEN ----------------
def play_level(screen, clock):

    return_btn = UIElement(
        center_position=(140, 560),
        font_size=24,
        text_rgb=WHITE,
        text="MAIN MENU",
        action=GameState.TITLE,
    )

    font = pygame.freetype.SysFont("consolas", 36, bold=True)

    while True:

        mouse_up = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_up = True

        screen.fill((15, 15, 15))

        font.render_to(
            screen,
            (180, 250),
            "GAME STARTS HERE",
            WHITE
        )

        ui_action = return_btn.update(
            pygame.mouse.get_pos(),
            mouse_up
        )

        if ui_action is not None:
            return ui_action

        return_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)


# ---------------- RUN GAME ----------------
if __name__ == "__main__":
    main()