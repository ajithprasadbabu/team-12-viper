from unittest import TestCase
from levelup.controller import GameController, DEFAULT_CHARACTER_NAME

class FakeGameMap(GameMap):
    def start_position():
        return Position(4,4)


class FakeCharacter(Character):
    def set_position(position: Position):
        self.position = position

    def get_position():
        return self.position    


class TestGameController(TestCase):
    def test_init(self):
        test_controller = GameController()
        self.assertEqual(DEFAULT_CHARACTER_NAME, test_controller.status.character.name)

    def test_create_default_character(self):
        test_controller = GameController()
        test_controller.create_character("")
        self.assertEqual(DEFAULT_CHARACTER_NAME, test_controller.status.character.name)

    def test_create_character(self):
        test_controller = GameController()
        expected_character_name = "ArbitraryName"
        test_controller.create_character(expected_character_name)
        self.assertEqual(expected_character_name, test_controller.status.character.name)

    def test_start_game(self):
        game_map = FakeGameMap()
        character = FakeCharacter()
        test_controller = GameController(game_map,character)
        test_controller.start_game()
        self.assertIsNotNone(test_controller.game_map)
        self.assertEquals(test_controller.character.get_position(), test_controller.game_map.start_position)
       