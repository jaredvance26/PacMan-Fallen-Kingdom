from pacmangame import constants
from pacmangame.action import Action
from pacmangame.point import Point
import random

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction().scale(constants.PACMAN_MOVE_SCALE)
        # ghost_dir = self._input_service.ghost_direction().scale(constants.MOVE_SCALE)
        
        pacman = cast['pacman'][0]
        blinky = cast['ghosts'][0]
        clyde = cast['ghosts'][1]
        inky = cast['ghosts'][2]
        pinky = cast['ghosts'][3]

        pacman.change_x = direction.get_x()
        pacman.change_y = direction.get_y()

        if pacman.change_x < 0:
            pacman.texture = pacman.textures[constants.TEXTURE_LEFT]
        elif pacman.change_x > 0:
            pacman.texture = pacman.textures[constants.TEXTURE_RIGHT]
        elif pacman.change_y < 0:
            pacman.texture = pacman.textures[constants.TEXTURE_BOTTOM]
        elif pacman.change_y > 0:
            pacman.texture = pacman.textures[constants.TEXTURE_TOP]

        # blinky.change_x = direction.get_x()
        # blinky.change_y = direction.get_y()