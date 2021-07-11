from pacmangame import constants
from pacmangame.action import Action
from pacmangame.point import Point


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                # It would be nice to add something to a base Actor class
                # to detect is_zero()...
                # if not actor.get_velocity().is_zero():

                if actor.change_x != 0 or actor.change_y != 0:
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        pacman = cast['pacman'][0]

        actor.center_x = actor.center_x + actor.change_x
        actor.center_y = actor.center_y + actor.change_y

        if self.change_x < 0:
            self.texture = self.textures[constants.TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[constants.TEXTURE_RIGHT]

