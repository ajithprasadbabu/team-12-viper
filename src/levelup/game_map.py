from dataclasses import dataclass


class GameMap:
    def __init__(self):
        self.row: int = 4
        self.col: int = 4

    def calculatePosition(self, position, direction):
        if direction == "n":
            pass
        elif direction == "s":
            pass  

    def validatePosition(self, position):
        self.row = position.x
        self.col = position.y
        return col >= 0 and col < 10 and row >= 0 and row < 10 
