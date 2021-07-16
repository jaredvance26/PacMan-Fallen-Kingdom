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
        self.count = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction().scale(constants.PACMAN_MOVE_SCALE)
        
        pacman = cast['pacman'][0]
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

       