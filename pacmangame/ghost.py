from pacmangame.point import Point
from pacmangame import constants
import arcade
import random
import math

class Ghost(arcade.Sprite):
    def __init__(self, image, x, y, wall_list):
        super().__init__(image, constants.ACTOR_SCALE)
        self.center_x = x
        self.center_y = y
        self.wall_list = wall_list
        self.wall_list = arcade.AStarBarrierList(self, self.wall_list, 8164800, 0, constants.MAX_X, 0, constants.MAX_Y)

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y
        self.path = arcade.astar_calculate_path(self.position,
                                                    player_sprite.position,
                                                    self.wall_list,
                                                    diagonal_movement=False)
        print(self.path,"->", self.position)

        # if self.center_x and self.center_y in self.path:
        #     self.center_x += self.change_x
        #     self.center_y += self.change_y 
        
        if random.randrange(150) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * 1
            self.change_y = math.sin(angle) * 1
