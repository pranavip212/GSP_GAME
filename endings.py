import pygame

def play_ending(screen, clock, choice, outcome):

    # --- Endings --- #
    if choice == "talk" and outcome == "good":
        print("talk, good ending")
    elif choice == "talk" and outcome == "bad":
        print("talk, bad ending")

    if choice == "fight" and outcome == "good":
        print("fight, good ending")
    elif choice == "fight" and outcome == "bad":
        print("fight, bad ending")

    # --- Main Game Loop --- #
    running = True
    while running:
        clock.tick(60)