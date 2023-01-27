from unittest import TestCase
from levelup.controller import GameController, DEFAULT_CHARACTER_NAME
from levelup.game_map import GameMap
from levelup.character import Character
from levelup.position import Position



class FakeCharacter(Character):
    def __init__(self, name):
        super()
        self.name = name

    def set_position(self, position):
        self.position = position

    def get_position(self):
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
        character = FakeCharacter(DEFAULT_CHARACTER_NAME)
        character.set_position(game_map.starting_position)  
        test_controller = GameController()
        test_controller.character = character

        test_controller.start_game()
        self.assertIsNotNone(test_controller.game_map)
        self.assertEqual(test_controller.status.character.position, test_controller.game_map.starting_position)
       