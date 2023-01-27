# Character class
import sys
sys.path.append('../src')
import unittest
from levelup.character import Character
from levelup.position import Position


class test_character(unittest.TestCase):
    def test_char_name(self):
        char = Character()
        self.assertEqual('Viper', char.name)
    def test_moveup_from_middle(self):
        char = Character()
        position = Position()
        position.setPosition(4, 4)
        char.setPosition(position)
        char.move('N')
        x,y = char.position.x, char.position.y
        self.assertEqual(x, 3)
        self.assertEqual(y,4)

    def test_moveup_from_top_left(self):
        char = Character()
        position = Position()
        position.setPosition(0, 0)
        char.setPosition(position)
        for i in ['N','W']:
            char.move(i)
            x,y = char.position.x, char.position.y
            self.assertEqual(x,0)
            self.assertEqual(y,0)
  
    def test_moveup_from_top_right(self):
        char = Character()
        position = Position()
        position.setPosition(0, 9)
        char.setPosition(position)
        for i in ['N','E']:
            char.move(i)
            x,y = char.position.x, char.position.y
            self.assertEqual(x,0)
            self.assertEqual(y,9)
    def test_moveup_from_bottom_left(self):
        char = Character()
        position = Position()
        position.setPosition(9, 0)
        char.setPosition(position)
        for i in ['S','W']:
            char.move(i)
            x,y = char.position.x, char.position.y
            self.assertEqual(x,9)
            self.assertEqual(y,0)
    def test_moveup_from_bottom_rigt(self):
        char = Character()
        position = Position()
        position.setPosition(9, 9)
        char.setPosition(position)
        for i in ['S','E']:
            char.move(i)
            x,y = char.position.x, char.position.y
            self.assertEqual(x,9)
            self.assertEqual(y,9)
if __name__ == "__main__":
      unittest.main()
