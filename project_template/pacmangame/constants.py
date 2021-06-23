import os

MAX_X = 800
MAX_Y = 600
SCREEN_TITLE = 'Pac-Man'

ACTOR_SCALE = .5
MOVE_SCALE = 7

PATH = os.path.dirname(os.path.abspath(__file__))
PACMAN_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-pac-man.png')
BLINKY_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-blinky.png')
CLYDE_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-clyde.png')
INKY_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-inky.png')
PINKY_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-pinky.png')
