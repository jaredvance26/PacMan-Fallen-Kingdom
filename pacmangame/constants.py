import os
import arcade

MAX_X = 635
MAX_Y = 770
SCREEN_TITLE = 'Pac-Man'

PATH = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(PATH, 'PacMan-Final.tmx')
MAP_NAME = 'Pac-Man'

ICON_SCALE = .75

ACTOR_SCALE = .22
MAP_SCALE = .25
MOVE_SCALE = 1.25

ICON_X = 30
ICON_Y = 15

PAC_MAN_X = MAX_X/2
PAC_MAN_Y = MAX_Y/1.2

BLINKY_X = MAX_X/2.1
CLYEDE_X = BLINKY_X - 25
INKY_X = BLINKY_X + 25
PINKY_X = BLINKY_X + 50

BLINKY_Y = MAX_Y/1.85
CLYEDE_Y = BLINKY_Y
INKY_Y = BLINKY_Y
PINKY_Y = BLINKY_Y

ICON_IMAGE = os.path.join(PATH, '..', 'images', 'pixel-pac-man-icon.png')

PACMAN_IMAGE = os.path.join(PATH, '..', 'images', 'character-pac-man.png')
PACMAN_LEFT = os.path.join(PATH, '..', 'images', 'character-pac-man-left.png')
PACMAN_TOP = os.path.join(PATH, '..', 'images', 'character-pac-man-top.png')
PACMAN_BOTTOM = os.path.join(PATH, '..', 'images', 'character-pac-man-bottom.png')

BLINKY_IMAGE = os.path.join(PATH, '..', 'images', 'character-blinky.png')
CLYDE_IMAGE = os.path.join(PATH, '..', 'images', 'character-clyde.png')
INKY_IMAGE = os.path.join(PATH, '..', 'images', 'character-inky.png')
PINKY_IMAGE = os.path.join(PATH, '..', 'images', 'character-pinky.png')


MOVE_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'sounds', 'pacman_chomp.wav'))
DEATH_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'sounds', 'pacman_death.wav'))
START_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'sounds', 'pacman_beginning.wav'))


TEXTURE_LEFT = 0
TEXTURE_BOTTOM = 1
TEXTURE_TOP = 2
TEXTURE_RIGHT = 3