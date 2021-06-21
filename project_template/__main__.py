import random
from PacMan import constants
from PacMan.output_service import ArcadeOutputService
import arcade

def main():
    output_service = ArcadeOutputService()
    output_service.clear_screen()

    arcade.run()

if __name__ == '__main__':
    main()