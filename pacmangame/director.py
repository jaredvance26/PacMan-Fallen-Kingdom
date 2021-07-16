import arcade
from pacmangame import constants
from pacmangame.pacman import PacMan
import random
from PIL import Image

win_pic = Image.open(constants.WIN_PIC)
lose_pic = Image.open(constants.LOSE_PIC)

class Director(arcade.Window):
    def __init__(self, cast, script, input_service):
        """ Initialize the game """
        super().__init__(constants.MAX_X, constants.MAX_Y, constants.SCREEN_TITLE)
        self._cast = cast
        self._script = script
        self._input_service = input_service
        self.wall_list = cast['walls']
        self.boarders = cast['boarders']
        self.food_list = cast['food']
        self.icon_list = cast['icon']
        self.blinky = cast['ghosts'][0]
        self.clyde = cast['ghosts'][1]
        self.inky = cast['ghosts'][2]
        self.pinky = cast['ghosts'][3]
        self.count = 0
        self.mod_count = 0

      

    def setup(self):
        """ Initalizes the screen """
        arcade.set_background_color(arcade.color.BLACK)
        arcade.play_sound(constants.START_SOUND)
        self.physics_engine = arcade.PhysicsEngineSimple(self._cast['pacman'][0],
                                                         self.wall_list)
        self.physics_engine_2 = arcade.PhysicsEngineSimple(self._cast['pacman'][0],
                                                         self.boarders)
        self.blinky_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][0], self.wall_list)
        self.clyde_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][1], self.wall_list)
        self.inky_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][2], self.wall_list)
        self.pinky_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][3], self.wall_list)
        self.blinky_engine2 = arcade.PhysicsEngineSimple(self._cast['ghosts'][0], self.boarders)
        self.clyde_engine2 = arcade.PhysicsEngineSimple(self._cast['ghosts'][1], self.boarders)
        self.inky_engine2 = arcade.PhysicsEngineSimple(self._cast['ghosts'][2], self.boarders)
        self.pinky_engine2 = arcade.PhysicsEngineSimple(self._cast['ghosts'][3], self.boarders)

    def on_update(self, delta_time):
        #Checks to see if any food is left, then closes the window if 0 or less is left. Otherwise, continues as normal.
        self.count += 1

        #GAME WINS CONDITION
        if len(self.food_list) <= 0:
            win_pic.show()
            arcade.close_window()

        #Creates walls and barriers
        self._cue_action("update")
        self.physics_engine.update()
        self.physics_engine_2.update()
        
        self.blinky_engine.update()
        self.clyde_engine.update()
        self.inky_engine.update()
        self.pinky_engine.update()

        self.blinky_engine2.update()
        self.clyde_engine2.update()
        self.inky_engine2.update()
        self.pinky_engine2.update()

        #Moves the ghosts up and out on first round
        if self.count < 100:
           self.blinky.change_y = constants.BLINKY_MOVE
           self.inky.change_y = constants.INKY_MOVE
           self.blinky.change_x = constants.BLINKY_MOVE
           self.inky.change_x = -constants.INKY_MOVE
           self.clyde.change_x = constants.CLYDE_MOVE
           self.pinky.change_x = -constants.PINKY_MOVE
           self.clyde.change_y = constants.CLYDE_MOVE
           self.pinky.change_y = constants.PINKY_MOVE
        else:
            self._cast['ghosts'][0].follow_sprite(self._cast['pacman'][0])
            self._cast['ghosts'][1].follow_sprite(self._cast['pacman'][0])
            self._cast['ghosts'][2].follow_sprite(self._cast['pacman'][0])
            self._cast['ghosts'][3].follow_sprite(self._cast['pacman'][0])

        if len(self.icon_list) <= 0:
            lose_pic.show()
            arcade.close_window()

        if self.count > 250:
            if len(self.wall_list) > 1:
                length = len(self.wall_list)
                self.wall_list.pop(random.randint(0, length-1))
                self.wall_list.pop(random.randint(0, length-1))
                self.count = 200


    def on_draw(self):
        self._cue_action("output")
        #Draw the map
        self.wall_list.draw()
        self.food_list.draw()

        self.boarders.draw()
        # self._cast['ghosts'][0].draw_path()


    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)