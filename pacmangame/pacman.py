from pacmangame.point import Point
from pacmangame import constants
import arcade

class PacMan(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PACMAN_IMAGE, constants.ACTOR_SCALE)

        self.center_x = constants.PAC_MAN_X 
        self.center_y = constants.PAC_MAN_Y

        
