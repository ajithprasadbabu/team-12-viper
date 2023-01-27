
from dataclasses import dataclass
from levelup.position import Position

@dataclass
class Character:
    name: str
    DEFAULT_CHAR_NAME = "Viper"
    def __init__(self, name=DEFAULT_CHAR_NAME):
        self.name = name
        self.position = None
        
    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def move(self, direction):
        direction = direction.name.lower()
        nPos_x = None
        nPos_y = None
        cPos_x = self.position.x
        cPos_y = self.position.y

        print(direction)

        if direction.startswith('n'):
            nPos_x = cPos_x - 1
            nPos_y = cPos_y
            print('You moved North')
        if direction.startswith('s'):
            nPos_x = cPos_x + 1
            nPos_y = cPos_y
            print('You moved South')
        if direction.startswith('w'):
            nPos_x = cPos_x
            nPos_y = cPos_y - 1
            print('You moved West')
        if direction.startswith('e'):
            nPos_x = cPos_x
            nPos_y = cPos_y + 1
            print('You moved East')
        else:
            return

        if nPos_y < 0 or nPos_y > 9: nPos_y = cPos_y
        if nPos_x < 0 or nPos_x > 9: nPos_x = cPos_x
        self.position.setPosition(nPos_x, nPos_y)
        self.cPos = self.position.getPosition()

