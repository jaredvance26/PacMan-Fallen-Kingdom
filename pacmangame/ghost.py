from pacmangame.point import Point
from pacmangame import constants
import arcade
import random
import math
import time

class Ghost(arcade.Sprite):
    def __init__(self, image, x, y, wall_list):
        super().__init__(image, constants.ACTOR_SCALE)
        self.center_x = x
        self.center_y = y
        self.wall_list = wall_list
        self.wall_list = arcade.AStarBarrierList(self, self.wall_list, (98 * constants.ACTOR_SCALE), 0, constants.MAX_X, 0, constants.MAX_Y)

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """
        print(player_sprite.position)
        self.path = arcade.astar_calculate_path(player_sprite.position,
                                                    self.position,
                                                    self.wall_list,
                                                    diagonal_movement=False)
        # print(self.path,"->", self.position)

        # if self.center_x and self.center_y in self.path:
        #     self.center_x += self.change_x
        #     self.center_y += self.change_y 
        if random.randrange(10) == 0:
            self.center_x = self.path[1][0]
            self.center_y = self.path[1][1]

        
    def draw_path(self):
        if self.path:
                arcade.draw_line_strip(self.path, arcade.color.BLUE, 2)
            
