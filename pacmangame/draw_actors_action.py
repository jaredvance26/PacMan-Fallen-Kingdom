from pacmangame.action import Action
from pacmangame import constants
from pacmangame.score import Score

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self.score = Score()

    def get_Score(self):
        return self.score

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen(self.score.get_Score())
        pacman = cast['pacman'][0]
        ghosts = cast['ghosts']
        icon = cast['icon']

        
        self._output_service.draw_actor(pacman)
        self._output_service.draw_actor(ghosts)
        self._output_service.draw_actor(icon)


