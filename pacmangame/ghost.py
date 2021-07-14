from pacmangame.point import Point
from pacmangame import constants
import arcade
import random
import math
import time

class Ghost(arcade.Sprite):
    def __init__(self, image, x, y, wall_list, move_speed):
        super().__init__(image, constants.ACTOR_SCALE)
        self.center_x = x
        self.center_y = y
        self.wall_list = wall_list
        self.wall_list = arcade.AStarBarrierList(self, self.wall_list, 64, 0, constants.MAX_X, 0, constants.MAX_Y)
        self.move_speed = move_speed

    def follow_sprite(self, player_sprite):
        """ Option that follows the path around the walls """
        self.path = arcade.astar_calculate_path(player_sprite.position,
                                                    self.position,
                                                    self.wall_list,
                                                    diagonal_movement=False)
        print(self.path,"->", player_sprite.center_x, player_sprite.center_y)

        if len(self.path) > 1:
            if self.center_x > player_sprite.center_x:
                self.change_x = -self.move_speed
            else:
                self.change_x = .5
            
            if self.center_y > player_sprite.center_y:
                self.change_y = -.5
            else:
                self.change_y = .5
        
        # if random.randrange(100) == 0:
        #     if len(self.path) > 1:
        #         self.center_x = self.path[1][0]
        #         self.center_y = self.path[1][1]
        #     else:
        #         self.change_x = -1
        #         self.change_y = -1
        # else:
        #     self.change_x = 1
        #     self.change_y = 1

        """Option that is slow and runs into walls"""
        # self.center_x += self.change_x
        # self.center_y += self.change_y

        # # Random 1 in 100 chance that we'll change from our old direction and
        # # then re-aim toward the player
        # if random.randrange(100) == 0:
        #     start_x = self.center_x
        #     start_y = self.center_y

        #     # Get the destination location for the bullet
        #     dest_x = player_sprite.center_x
        #     dest_y = player_sprite.center_y

        #     # Do math to calculate how to get the bullet to the destination.
        #     # Calculation the angle in radians between the start points
        #     # and end points. This is the angle the bullet will travel.
        #     x_diff = dest_x - start_x
        #     y_diff = dest_y - start_y
        #     angle = math.atan2(y_diff, x_diff)

        #     # Taking into account the angle, calculate our change_x
        #     # and change_y. Velocity is how fast the bullet travels.
        #     self.change_x = math.cos(angle) * constants.MOVE_SCALE
        #     self.change_y = math.sin(angle) * constants.MOVE_SCALE

        
    def draw_path(self):
        if self.path:
                arcade.draw_line_strip(self.path, arcade.color.BLUE, 2)
            
