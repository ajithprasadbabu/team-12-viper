from dataclasses import dataclass


@dataclass
class GameMap:
    row: int
    col: int

    def calculatePosition(self, direction):
        pass