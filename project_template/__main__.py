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
from pacmangame.ghost import Ghost

import arcade
import random

def main():
    output_service = ArcadeOutputService()
    input_service = ArcadeInputService()
    
    cast = {}
    ghost_list = arcade.SpriteList()
    pacman = PacMan()


    
    pinky = Ghost(constants.PINKY_IMAGE, constants.PINKY_X, constants.PINKY_Y)
    blinky = Ghost(constants.BLINKY_IMAGE, constants.BLINKY_X, constants.BLINKY_Y)
    clyde = Ghost(constants.CLYDE_IMAGE, constants.CLYEDE_X, constants. CLYEDE_Y)
    inky = Ghost(constants.INKY_IMAGE, constants.INKY_X, constants.INKY_Y)
    
    ghost_list.append(blinky)
    ghost_list.append(clyde)
    ghost_list.append(inky)
    ghost_list.append(pinky)

   

    cast['pacman'] = [pacman]
    cast['ghosts'] = ghost_list
    

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