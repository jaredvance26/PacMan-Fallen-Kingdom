import random
from pacmangame import constants
from pacmangame import commands
from pacmangame.action import Action
import arcade
from pacmangame.draw_actors_action import DrawActorsAction
from pacmangame.commands import Commands

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, score):
        """sets a variable to track how many rotations the game has gone through since the last time a sound was played for food collection"""
        self.soundCount = 0
        self.score = score
        self.Command_Holder = Commands()
        self.score_step = 403

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
            self.score.change_Score(self.score_step)
            if self.soundCount <= 0:
                arcade.play_sound(constants.MOVE_SOUND)
                self.soundCount = 33
        
        #Handle collisions to ghosts
        if len(pacman.collides_with_list(ghosts)) > 0:
            arcade.play_sound(constants.DEATH_SOUND)
            if len(icons) <= 0:
                arcade.close_window()
            else:
                icons.pop()
                self.Command_Holder.reset_game(cast)
                self.score_step = int(round(self.score_step/2, 0))
        