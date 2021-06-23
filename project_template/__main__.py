from pacmangame import constants
from pacmangame.output_service import ArcadeOutputService
from pacmangame.director import Director
from pacmangame.pacman import PacMan
from pacmangame.draw_actors_action import DrawActorsAction

import arcade
import random

def main():
    output_service = ArcadeOutputService()
    output_service.clear_screen()
    
    cast = {}
    pacman = PacMan()
    cast['pacman'] = pacman

    script = {}
    draw_actors_action = DrawActorsAction(output_service)
    script["output"] = [draw_actors_action]

    director = Director(cast, script)

    arcade.run()

if __name__ == '__main__':
    main()