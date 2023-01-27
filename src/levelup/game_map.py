from dataclasses import dataclass
from levelup.position import Position

MIN_ROW = 0
MAX_ROW = 9
MIN_COL = 0
MAX_COL = 9


class GameMap:
    starting_position: Position = Position()

    def __init__(self):
        self.row: int = MAX_ROW
        self.col: int = MAX_COL
        self.starting_position.setPosition(4,4)

    def calculatePosition(self, position, direction):
        self.row = position.x
        self.col = position.y
        
        if direction == "n":
            row = self.row - 1
            if self.validatePosition(row, self.col):
                self.row = row

        elif direction == "s":
            row = self.row + 1
            if self.validatePosition(row, self.col):
                self.row = row

        elif direction == "e":
            col = self.col + 1
            if self.validatePosition(self.row, col):
                self.col = col

        elif direction == "w":
            col = self.col - 1
            if self.validatePosition(self.row, col):
                self.col = col 

    def validatePosition(self, row, col):
        return col >= MIN_COL and col <= MAX_COL and row >= MIN_ROW and row <= MAX_ROW 
