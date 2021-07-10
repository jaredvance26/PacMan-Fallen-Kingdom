import random
from pacmangame import constants
from pacmangame.action import Action
from pacmangame.point import Point
import arcade

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        """sets a variable to track how many rotations the game has gone through since the last time a sound was played for food collection"""
        self.soundCount = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.soundCount -= 1
        pacman = cast['pacman'][0]
        ghosts = cast['ghosts']
        walls = cast['walls']
        food = cast['food']
        icons = cast['icon']

    
        if pacman.top > constants.MAX_Y:
            pacman.top = constants.MAX_Y
        elif pacman.right > constants.MAX_X:
            pacman.left = 0
        elif pacman.left < 0:
            pacman.right = constants.MAX_X
        elif pacman.bottom < 0:
            pacman.bottom = 0
    
        #Handle collisions with food
        food_hit_list = arcade.check_for_collision_with_list(pacman, food)
        for f in food_hit_list:
            f.remove_from_sprite_lists()
            if self.soundCount <= 0:
                arcade.play_sound(constants.MOVE_SOUND)
                self.soundCount = 33
        
        #Handle collisions to ghosts
        if len(pacman.collides_with_list(ghosts)) > 0:
            arcade.play_sound(constants.DEATH_SOUND)
            icons.pop()


            

            
            
        