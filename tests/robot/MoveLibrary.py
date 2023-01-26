from levelup.controller import GameController
from levelup.controller import Direction

start_x: int
start_y: int
start_move_count: int

class MoveLibrary:

    # Pre-Conditions
    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position

    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position
    
    def starting_move_count(self, move_count):
        self.start_move_count = move_count

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.set_character_position((self.start_x, self.start_y))
        self.controller.set_move_count(self.start_move_count)
        self.controller.move(Direction[direction])

    # Post-Conditions
    def character_xposition_should_be(self, expected):
        end_x = self.controller.status.current_position[0]
        if end_x != expected:
            raise AssertionError("1. %s != %s" % (end_x, expected))

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position[0]
        if end_y != expected:
            raise AssertionError("2. %s != %s" % (end_y, expected))

    def ending_move_count(self, expected):
        actual_move_count = self.controller.status.move_count
        if actual_move_count != expected:
            raise AssertionError("3. %s != %s" % (actual_move_count, expected))