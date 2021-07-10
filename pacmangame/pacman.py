from pacmangame.point import Point
from pacmangame import constants
import arcade

class PacMan(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = constants.ACTOR_SCALE
        self.textures = []


        texture = arcade.load_texture(constants.PACMAN_IMAGE)
        self.textures.append(texture)

        self.center_x = constants.PAC_MAN_X 
        self.center_y = constants.PAC_MAN_Y

        if self.change_x < 0:
            self.texture = self.textures[constants.PACMAN_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[constants.PACMAN_IMAGE]

        self.texture = texture



        
