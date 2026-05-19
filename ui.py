import pygame
import pygame.freetype
from constants import *
pygame.init()


# ---------------- TYPEWRITER TEXT ----------------
class DialogueBox:
    def __init__(self, rect, font_size=28):

        self.rect = pygame.Rect(rect)

        self.font = pygame.freetype.SysFont(
            "consolas",
            font_size,
            bold=True
        )

        self.text = ""

        # current visible letters
        self.visible_characters = 0

        # controls typing speed
        self.text_speed = 2

        self.finished = False

    def set_text(self, text):
#loads the text gping into the box
        self.text = text
        self.visible_characters = 0
        self.finished = False

    def update(self):
        """Reveals text slowly each frame"""

        if self.visible_characters < len(self.text):
            self.visible_characters += self.text_speed
        else:
            self.finished = True

    def draw(self, screen):

        # dialogue background box
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        pygame.draw.rect(screen, (180, 30, 30), self.rect, 3)

        # only show currently revealed text
        visible_text = self.text[:self.visible_characters]

        self.font.render_to(
            screen,
            (self.rect.x + 20, self.rect.y + 20),
            visible_text,
            (255, 255, 255)
        )