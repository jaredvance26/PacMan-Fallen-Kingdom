from pacmangame.point import Point
from pacmangame import constants
import arcade

class PacMan(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = constants.ACTOR_SCALE
        self.textures = []

        #Facing Left
        texture = arcade.load_texture(constants.PACMAN_LEFT)
        self.textures.append(texture)

        #Facing Bottom 
        texture = arcade.load_texture(constants.PACMAN_BOTTOM)
        self.textures.append(texture)

        #Facing Top
        texture = arcade.load_texture(constants.PACMAN_TOP)
        self.textures.append(texture)
        
        #Facing Right
        texture = arcade.load_texture(constants.PACMAN_IMAGE)
        self.textures.append(texture)

        self.center_x = constants.PAC_MAN_X 
        self.center_y = constants.PAC_MAN_Y


        self.texture = texture



        
