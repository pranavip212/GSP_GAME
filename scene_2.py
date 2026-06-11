import player_data
import pygame.freetype
from game_states import GameState
from images import *
from ui import DialogueBox


def play_intro(screen, clock):

    fade_alpha = 255

    dialogue_lines = [

        [("Running into the corridor, the school is crawling with the undead in uniforms.", WHITE)],

        [("Distracted, you run into a tall figure...", WHITE)],

        [("Expecting the worst, you are shocked when you meet Mila's dark, tired eyes.", WHITE)],

        [("MILA: O.M.G! What are you doing here?", PURPLE)],

        [("YOU: RUNNING? HELLO? ZOMBIES???", WHITE)],

        [("MILA: OH RIGHT!!", PURPLE)],


        [("Mila's cold hand grabs yours and pulls you into the kitchen, locking the door.", WHITE)],

        [("After catching your breath, Mila insists on making you breakfast.", WHITE)],

        [("You and Mila survived history class together and have been trauma-bonded ever since.", WHITE)],

        [("Naturally, she is your first and only friend at this new school...", WHITE)],

        [("...even if she seems a little strange...", WHITE)],

        [("Mila interrupts your thoughts and slides a plate in front of you.", WHITE)],

        [("The scrambled eggs look fine, but the bacon... it's practically raw.", WHITE)],

        [('MILA: You like it crispy, right?', RED)],

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

    eat_button = pygame.Rect((40, 240, 250, 60))
    refuse_button = pygame.Rect((40, 310, 250, 60))
    knife_button = pygame.Rect((40, 380, 250, 60))
    font = pygame.freetype.SysFont("consolas", 28, bold=True)

    #choice loop
    while True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            # Choices
            if show_choices and event.type == pygame.MOUSEBUTTONDOWN:

                if eat_button.collidepoint(event.pos):
                    return play_eat_bacon(screen, clock)

                elif refuse_button.collidepoint(event.pos):
                    return play_refuse_food(screen, clock)

                elif knife_button.collidepoint(event.pos):
                    return play_grab_knife(screen, clock)

            # dialogue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not show_choices:
                    current_line += 1

                    if current_line < len(dialogue_lines):
                        dialogue_box.set_text(dialogue_lines[current_line])
                    else:
                            show_choices = True

        screen.blit(day_hallway, (0, 0))

        if current_line >= 3:
            screen.blit(mila_normal_lit,(450, 100))

        if current_line >= 8:
            screen.blit(breakfast,(0, 0))

        if current_line >=12:
            screen.blit(plate_of_bacon, (0,0))

        overlay = pygame.Surface((WIDTH, HEIGHT))

        overlay.fill((20, 0, 0))
        overlay.set_alpha(40)

        screen.blit(overlay, (0, 0))

        if fade_alpha > 0:
            fade_surface = pygame.Surface(
                (WIDTH, HEIGHT)
            )

            fade_surface.fill(BLACK)

            fade_surface.set_alpha(
                fade_alpha
            )

            screen.blit(
                fade_surface,
                (0, 0)
            )

            fade_alpha -= 2

        if show_choices:
            pygame.draw.rect(
                screen, BLACK, eat_button
            )

            pygame.draw.rect(
                screen, BLACK, refuse_button
            )

            pygame.draw.rect(
                screen, BLACK, knife_button
            )

            pygame.draw.rect(
                screen, DARK_RED, eat_button, 3
            )

            pygame.draw.rect(
                screen, DARK_RED, refuse_button, 3
            )

            pygame.draw.rect(
                screen, DARK_RED, knife_button, 3
            )

            eat_color = RED if eat_button.collidepoint(
                pygame.mouse.get_pos()
            ) else WHITE

            refuse_color = RED if refuse_button.collidepoint(
                pygame.mouse.get_pos()
            ) else WHITE

            knife_color = RED if knife_button.collidepoint(
                pygame.mouse.get_pos()
            ) else WHITE

            font.render_to(
                screen,
                (61, 260),
                "Eat Bacon",
                eat_color
            )

            font.render_to(
                screen,
                (61, 330),
                "Refuse Food",
                refuse_color
            )

            font.render_to(
                screen,
                (61, 400),
                "Grab Knife",
                knife_color
            )

        dialogue_box.update()
        dialogue_box.draw(screen)

        pygame.display.flip()




def play_eat_bacon (screen, clock):
    player_data.trust =+ 4

    dialogue_lines = [
        [("You pick up your fork and try the bacon.", WHITE)],
        [("You feel your stomach churn...", WHITE)],
        [("You feel stronger after eating, though, even if it's nasty.", WHITE)],
        [("It's cold and slimy, but Mila nods approvingly.", WHITE)],
        [("You've gained her trust...", WHITE)],
        [("Suddenly, you are interrupted by a scream in the hallway.", WHITE)]
    ]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])





    # check runtime
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_line += 1

                    if current_line < len(dialogue_lines):
                        dialogue_box.set_text(dialogue_lines[current_line])
                    else:
                            return GameState.GAME

        screen.blit(plate_of_bacon, (0, 0))
        if current_line >= 3:
            screen.blit(kitchen, (0,0))
            screen.blit(mila_happy_lit, (450, 100))


        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()

def play_refuse_food (screen, clock):
    player_data.trust -=2
    dialogue_lines = [
        [("You push the plate away, feeling uneasy.", WHITE)],
        [("Mila shrugs and continues eating, but her eyes linger on you for too long.", WHITE)],
        [("[-2 TRUST]", DARK_RED)],
        [("Suddenly, the tension is broken by a scream in the hallway.", WHITE)],
    ]

    current_line = 0
    dialogue_box = DialogueBox((40, 450, 720, 120))
    dialogue_box.set_text(dialogue_lines[current_line])


    # check runtime
    while True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.KEYDOWN:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_line += 1

                        if current_line < len(dialogue_lines):
                            dialogue_box.set_text(dialogue_lines[current_line])
                        else:
                            return GameState.GAME

        screen.blit(kitchen, (0, 0))
        if current_line >= 1:
            screen.blit(mila_pensive_lit, (450, 100))

        # visuals
        # fix lines here
        dialogue_box.update()
        dialogue_box.draw(screen)
        pygame.display.flip()

def play_grab_knife(screen, clock):
    player_data.trust -=5
    player_data.has_knife = True



    dialogue_lines = [

    [("You look around the kitchen, an idea forming...", WHITE)],

    [("YOU: Mila, could you please grab me some pepper from the pantry?", RED)],

    [("MILA: Sure, no problem.", PURPLE)],

    [("When she is out of sight, you jump up and grab the sharpest knife you see...", WHITE)],

    [("You wrap it in a paper towel and hide it in your sock.", WHITE)],

    [("With a racing heart, you sit back down.", WHITE)],

    [("However, Mila notices the open knife drawer...", WHITE)],

    [("MILA: Uh hey... what are you doing there?", PURPLE)],

    [("YOU: Uh... um...", RED)],

    [("[-5 TRUST]", DARK_RED)],

    [("Suddenly, the tension is broken by a scream in the hallway.", WHITE)]

    ]

    current_line = 0

    dialogue_box = DialogueBox(
        (40, 450, 720, 120)
    )

    dialogue_box.set_text(
        dialogue_lines[current_line]
    )

    while True:

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.KEYDOWN:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_line += 1

                        if current_line < len(dialogue_lines):
                            dialogue_box.set_text(dialogue_lines[current_line])

                        else:
                            return GameState.GAME

        screen.fill(BLACK)

        dialogue_box.update()
        dialogue_box.draw(screen)

        pygame.display.flip()

