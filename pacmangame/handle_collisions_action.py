import random
from pacmangame import constants
from pacmangame.action import Action
import arcade

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        pacman = cast['pacman'][0]
        ghosts = cast['ghosts']
        walls = cast['walls']

        if pacman.top > constants.MAX_Y:
            pacman.top = constants.MAX_Y
        elif pacman.right > constants.MAX_X:
            pacman.left = 0
        elif pacman.left < 0:
            pacman.right = constants.MAX_X
        elif pacman.bottom < 0:
            pacman.bottom = 0
        
        #Handle collisions to the wall
        # for i in walls: 
        #     if len(pacman.collides_with_list(walls)) > 0:
        #         pacman.center_x = i
        #         pacman.center_y = i
        
        #Handle collisions to ghosts
        if len(pacman.collides_with_list(ghosts)) > 0:
            arcade.play_sound(constants.DEATH_SOUND)
            arcade.close_window()
            
        