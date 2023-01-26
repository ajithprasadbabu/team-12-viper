from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def getPosition (self):
        return (self, x, self, y)

    def setgPosition (self, x, y):
        self.x = x
        self.y = y
