
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
        direction = direction.lower()
        nPos_x = None
        nPos_y = None
        cPos_x = self.position.x
        cPos_y = self.position.y

        if direction == 'n':
            nPos_x = cPos_x - 1
            nPos_y = cPos_y
        if direction == 's':
            nPos_x = cPos_x + 1
            nPos_y = cPos_y
        if direction == 'w':
            nPos_x = cPos_x
            nPos_y = cPos_y - 1
        if direction == 'e':
            nPos_x = cPos_x
            nPos_y = cPos_y + 1

        if nPos_y < 0 or nPos_y > 9: nPos_y = cPos_y
        if nPos_x < 0 or nPos_x > 9: nPos_x = cPos_x
        self.position.setPosition(nPos_x, nPos_y)
        self.cPos = self.position.getPosition()

