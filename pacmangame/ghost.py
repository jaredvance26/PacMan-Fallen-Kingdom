from pacmangame.point import Point
from pacmangame import constants
import arcade
import random

class Ghost(arcade.Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, constants.ACTOR_SCALE)

        self.center_x = x
        self.center_y = y

        
