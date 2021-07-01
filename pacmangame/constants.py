import os
import arcade

MAX_X = 650
MAX_Y = 770
SCREEN_TITLE = 'Pac-Man'

PATH = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(PATH, 'PacMan-Final.tmx')
MAP_NAME = 'Pac-Man'

ACTOR_SCALE = .20
MOVE_SCALE = 7
STAGE_SCALE = .26

BLINKY_X = MAX_X/2
CLYEDE_X = MAX_X/2 - 50
INKY_X = MAX_X/2 + 50
PINKY_X = MAX_X/2 + 100

BLINKY_Y = MAX_Y/2
CLYEDE_Y = MAX_Y/2   
INKY_Y = MAX_Y/2
PINKY_Y = MAX_Y/2


PACMAN_IMAGE = os.path.join(PATH, '..', 'images', 'character-pac-man.png')
BLINKY_IMAGE = os.path.join(PATH, '..', 'images', 'character-blinky.png')
CLYDE_IMAGE = os.path.join(PATH, '..', 'images', 'character-clyde.png')
INKY_IMAGE = os.path.join(PATH, '..', 'images', 'character-inky.png')
PINKY_IMAGE = os.path.join(PATH, '..', 'images', 'character-pinky.png')
MOVE_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'sounds', 'pacman_chomp.wav'))
DEATH_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'sounds', 'pacman_death.wav'))
START_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'sounds', 'pacman_beginning.wav'))