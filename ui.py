import pygame
import pygame.freetype
from constants import *
pygame.init()

def speaker(name, color, dialogue):
    return [
        (f"{name}: ", color),
        (dialogue, WHITE)
    ]

# typewriter effect on screen
class DialogueBox:
    def __init__(self, rect, font_size=28):

        self.rect = pygame.Rect(rect)

        self.font = pygame.freetype.SysFont(
            "consolas",
            font_size,
            bold=True
        )

        self.text_segments = []
        self.full_text = ""

        # current visible letters
        self.visible_characters = 0

        # controls typing speed
        self.text_speed = 1

        self.finished = False

    def set_text(self, text_segments):
        #loads the text gping into the box
        self.text_segments = text_segments

        # combine all text together
        self.full_text = "".join(
            text for text, color in text_segments
        )

        self.visible_characters = 0
        self.finished = False

    def update(self):
        """Reveals text slowly each frame"""

        if self.visible_characters < len(self.full_text):
            self.visible_characters += self.text_speed
        else:
            self.finished = True

    def draw(self, screen):
        #wrap text code fix was ai generated
        # dialogue background box
        pygame.draw.rect(screen, BLACK, self.rect)
        pygame.draw.rect(screen, (180, 30, 30), self.rect, 3)

        start_x = self.rect.x + 20
        x = start_x
        y = self.rect.y + 20

        max_width = self.rect.width - 40
        line_height = self.font.get_sized_height() + 5

        chars_drawn = 0

        for text, color in self.text_segments:

            chars_left = self.visible_characters - chars_drawn

            if chars_left <= 0:
                break

            partial_text = text[:chars_left]

            words = partial_text.split(" ")

            for word in words:

                word_text = word + " "

                word_width = self.font.get_rect(word_text).width

                # Wrap to next line if needed
                if x + word_width > start_x + max_width:
                    x = start_x
                    y += line_height

                self.font.render_to(
                    screen,
                    (x, y),
                    word_text,
                    color
                )

                x += word_width

            chars_drawn += len(partial_text)
