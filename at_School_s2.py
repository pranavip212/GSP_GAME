import pygame
from constants import *
from game_states import GameState
from ui import DialogueBox



def at_School(screen, clock):
    # images
    day_hallway = pygame.image.load('assets/images/day_hallway.png').convert()
    day_hallway = pygame.transform.scale(day_hallway, (WIDTH, HEIGHT))
    mila_standing = pygame.image.load("assets/images/mila_standing_bg.png").convert_alpha()
    mila_standing = pygame.transform.scale(mila_standing, (300, 300))

    # fade
    fade_alpha = 255

    dialogue_lines = [

        [("Running into the corridor, you look around at the school crawling with undead in uniforms", WHITE)],

        [("Distracted, you run into a tall figure...", WHITE)],

        [("Expecting the worst, you are shocked when you meet Mila's dark, tired eyes", WHITE)],

        speaker(
            "Mila",
            PURPLE,
            "O.M.G! What are you doing here?"
        ),

        speaker(
            "You",
            RED,
            "RUNNING? HELLO? ZOMBIES???"
        ),

        speaker(
            "Mila",
            PURPLE,
            "OH RIGHT!"
        ),

        [("Mila's cold hand grabs yours and you run into the kitchen, locking the door.", WHITE)],

        [("After catching your breath, you follow Mila to the stove, where she insists on making breakfast.", WHITE)],

        [("You and Mila sat together in history class, and are trauma bonded after surviving that class.", WHITE)],

        [(
         "Naturally, she is your first and only friend at this new school even if she seems a little strange…", WHITE)],

        [("Mila interrupts your thoughts and slides a plate in front of you.", WHITE)],

        [("The scrambled eggs look fine, but the bacon… it's practically raw.", WHITE)],

        speaker(
            "Mila",
            PURPLE,
            "You like it crispy, right?"
        ),

        [("She asks, already biting into a bloody strip.", WHITE)],

        [("You hesitate. Mila always seemed a little weird, but this?", WHITE)],

        [("What will you do?", DARK_RED)]

    ]


    current_line = 0

    # create dialogue box
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])

    # choice buttons only appear later
    show_choices = False

def title_screen(screen, clock):

    eat_bacon_btn = UIElement(
        center_position=(WIDTH // 2, 380),
        font_size=40,
        text_rgb=WHITE,
        text="START",
        action=GameState.INTRO,
    )

    dont_eat_btn = UIElement(
        center_position=(WIDTH // 2, 470),
        font_size=40,
        text_rgb=WHITE,
        text="QUIT",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    font = pygame.freetype.SysFont("consolas", 32, bold=True)

    running = True

    while running:

        # limiting fps

        clock.tick(60)

        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
                running = False

            # key pressed
            if event.type == pygame.KEYDOWN:

                # SPACE advances dialogue
                if event.key == pygame.K_SPACE:

                    # if line still typing, finsh it
                    if not dialogue_box.finished:

                        dialogue_box.visible_characters = len(
                            dialogue_box.text
                        )

                    # otherwise go next line
                    else:

                        current_line += 1

                        # if dialogue remains
                        if current_line < len(dialogue_lines):

                            dialogue_box.set_text(
                                dialogue_lines[current_line]
                            )

                        # intro finished
                        else:
                            return GameState.GAME

        # draw bedroom
        screen.blit(bedroom, (0, 0))

        # reveal zombie w dialouge pacing
        if current_line >= 3:
            screen.blit(
                zombie,
                (250, 100)
            )

        # dark red horror overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))

        overlay.fill((20, 0, 0))

        overlay.set_alpha(40)

        screen.blit(overlay, (0, 0))
        # used chat for help with fade
        # fade from black at beginning
        if fade_alpha > 0:
            fade_surface = pygame.Surface((WIDTH, HEIGHT))

            fade_surface.fill(BLACK)

            fade_surface.set_alpha(fade_alpha)

            screen.blit(fade_surface, (0, 0))

            # slowly remove black screen
            fade_alpha -= 2

        # update typewriter effect
        dialogue_box.update()

        dialogue_box.draw(screen)

        # update screen
        pygame.display.flip()