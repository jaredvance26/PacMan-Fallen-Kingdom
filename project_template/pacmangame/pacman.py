from pacmangame.point import Point
from pacmangame import constants
import arcade

class PacMan(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PACMAN_IMAGE)

        self.center_x = int(constants.MAX_X/2)
        self.center_y = int(constants.MAX_Y/2)

        
