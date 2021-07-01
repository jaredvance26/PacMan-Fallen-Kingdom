from pacmangame.point import Point
from pacmangame import constants
import arcade

class PacMan(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PACMAN_IMAGE, constants.ACTOR_SCALE)

        self.center_x = int(constants.MAX_X/3)
        self.center_y = int(constants.MAX_Y/4)

        
