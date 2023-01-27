from levelup.controller import GameController


class GameControllerLibrary:
    def initialize_controller(self):
        self.controller = GameController()

    def create_character_with_name(self, charactername):
        self.controller.create_character(charactername)

    def character_name_should_be(self, expected):
        if self.controller.status.character.name != expected:
            raise AssertionError(
                "%s != %s" % (self.controller.status.character.name, expected)
            )

    def initialize_map(self):
        if not self.controller.game_map:
            raise AssertionError("map not initialized")
    
    def start_game(self):
        self.controller.start_game()

    def character_position_at_starting_position(self):
        if (self.controller.status.character.position != self.controller.game_map.starting_position):
            raise AssertionError("Character is not at map starting position")