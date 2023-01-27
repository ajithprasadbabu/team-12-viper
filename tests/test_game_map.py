from unittest import TestCase
from levelup.game_map import GameMap


class TestGameMap(TestCase):
    def setUp(self):
        self.gamemap = GameMap()

    def test_validatePosition(self):
        self.assertTrue(self.gamemap.validatePosition(0,0))
        self.assertTrue(self.gamemap.validatePosition(4,4))
        self.assertTrue(self.gamemap.validatePosition(9,9))
        self.assertFalse(self.gamemap.validatePosition(9,10))
        self.assertFalse(self.gamemap.validatePosition(10,9))
        self.assertFalse(self.gamemap.validatePosition(-1,0))
        self.assertFalse(self.gamemap.validatePosition(0,-1))
        

    # def test_calculatePosition(self):
    #     self.gamemap.


if __name__ == '__main__':
    unittest.main()