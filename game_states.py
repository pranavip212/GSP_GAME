from enum import Enum

class GameState(Enum):
    TITLE = 0
    INTRO = 1
    FIGHT = 2
    GAME = 3
    QUIT = 4