from dataclasses import dataclass


class Position:

    def __init__(self):
        self.x = -1
        self.y = -1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPosition (self):
        return (self.x, self.y)

    def setPosition(self, x, y):
        self.x = x
        self.y = y
