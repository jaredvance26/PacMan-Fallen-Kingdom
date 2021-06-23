from pacmangame import constants
from pacmangame.point import Point
from pacmangame.control_actors_action import ControlActorsAction
from pacmangame.draw_actors_action import DrawActorsAction
from pacmangame.handle_collisions_action import HandleCollisionsAction
from pacmangame.move_actors_action import MoveActorsAction
from pacmangame.input_service import ArcadeInputService
from pacmangame.output_service import ArcadeOutputService
from pacmangame.pacman import PacMan
from pacmangame.director import Director

import arcade
import random

def main():
    output_service = ArcadeOutputService()
    input_service = ArcadeInputService()
    
    cast = {}
    pacman = PacMan()
    cast['pacman'] = [pacman]

    script = {}
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    control_actors_action = ControlActorsAction(input_service)

    script["output"] = [draw_actors_action]
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]

    director = Director(cast, script, input_service)
    director.setup()

    arcade.run()

if __name__ == '__main__':
    main()