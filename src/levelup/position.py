from dataclasses import dataclass


class Position:
    def __init__(self):
        self.x: int
        self.y: int

    def getPosition (self):
        return (self.x, self.y)

    def setPosition (self, x, y):
        self.x = x
        self.y = y
