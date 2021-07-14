import arcade
from pacmangame import constants
from pacmangame.pacman import PacMan


class Director(arcade.Window):
    def __init__(self, cast, script, input_service):
        """ Initialize the game """
        super().__init__(constants.MAX_X, constants.MAX_Y, constants.SCREEN_TITLE)
        self._cast = cast
        self._script = script
        self._input_service = input_service
        self.wall_list = cast['walls']
        self.food_list = cast['food']
        self.icon_list = cast['icon']
        self.blinky = cast['ghosts'][0]
        self.clyde = cast['ghosts'][1]
        self.inky = cast['ghosts'][2]
        self.pinky = cast['ghosts'][3]
        self.count = 0

    def setup(self):
        """ Initalizes the screen """
        arcade.set_background_color(arcade.color.BLACK)
        arcade.play_sound(constants.START_SOUND)
        self.physics_engine = arcade.PhysicsEngineSimple(self._cast['pacman'][0],
                                                         self.wall_list)
        self.blinky_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][0], self.wall_list)
        self.clyde_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][1], self.wall_list)
        self.inky_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][2], self.wall_list)
        self.pinky_engine = arcade.PhysicsEngineSimple(self._cast['ghosts'][3], self.wall_list)

    def on_update(self, delta_time):
        #Checks to see if any food is left, then closes the window if 0 or less is left. Otherwise, continues as normal.
        #GAME WINS CONDITION
        if len(self.food_list) <= 0:
            arcade.close_window()

        self._cue_action("update")
        self.physics_engine.update()
        self.blinky_engine.update()
        self.clyde_engine.update()
        self.inky_engine.update()
        self.pinky_engine.update()

        if self.count < 100:
           self.blinky.change_y = 1
           self.inky.change_y = 1
           self.blinky.change_x = 1
           self.inky.change_x = -1
           self.clyde.change_x = 1
           self.pinky.change_x = -1
           self.clyde.change_y = 1
           self.pinky.change_y = 1
           self.count += 1
        else:
            self._cast['ghosts'][0].follow_sprite(self._cast['pacman'][0])
            self._cast['ghosts'][1].follow_sprite(self._cast['pacman'][0])
            self._cast['ghosts'][2].follow_sprite(self._cast['pacman'][0])
            self._cast['ghosts'][3].follow_sprite(self._cast['pacman'][0])

        if len(self.icon_list) <= 0:
            arcade.close_window()


    def on_draw(self):
        self._cue_action("output")
        #Draw the map
        self.wall_list.draw()
        self.food_list.draw()
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