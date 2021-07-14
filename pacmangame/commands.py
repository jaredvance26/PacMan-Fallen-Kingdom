from pacmangame.constants import *

class Commands:
    def __init__(self):
        pass

    def reset_game(self, cast):
        ghosts = cast["ghosts"]

        cast["pacman"][0].center_x = PAC_MAN_X
        cast["pacman"][0].center_y = PAC_MAN_Y

        ghosts[0].center_x = BLINKY_X
        ghosts[0].center_y = BLINKY_Y
        ghosts[1].center_x = CLYEDE_X
        ghosts[1].center_y = CLYEDE_Y
        ghosts[2].center_x = INKY_X
        ghosts[2].center_y = INKY_Y
        ghosts[3].center_x = PINKY_X
        ghosts[3].center_y = PINKY_Y