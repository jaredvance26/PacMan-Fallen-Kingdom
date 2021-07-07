from pacmangame.point import Point
from pacmangame import constants
import arcade

class Icon(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.ICON_IMAGE, constants.ICON_SCALE)

        self.center_x = x
        self.center_y = y
