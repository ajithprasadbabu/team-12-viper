from dataclasses import dataclass
from position import Position

@dataclass
class Character:
    name: str
    DEFAULT_CHAR_NAME = "Viper"
    def __init__(self, name=DEFAULT_CHAR_NAME):
        self.name = name
        self.position = Position()
        self.cPos = self.getPosition()
        
    def setPosition(self,x,y):
        self.position.setPosition(x,y)

    def getPosition(self):
        return self.position.getPosition()

    def move(self, direction):
        direction = direction.lower()
        nPos = (-1,-1)
