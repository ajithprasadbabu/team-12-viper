from enum import Enum
from dataclasses import dataclass
from levelup.character import Character

DEFAULT_CHARACTER_NAME = "Character"
ARBITRARY_INVALID_INITIALIZED_POSITION = (-1,-1)

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    current_position: tuple = ARBITRARY_INVALID_INITIALIZED_POSITION
    move_count: int = 0


class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()
        self.game_map = None
    
    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for testing")
        # TODO: IMPLEMENT THIS

    def create_character(self, character_name: str) -> None:
        if not character_name:
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        print(f"Moved {direction.name}")

    def set_move_count(self, move_count) -> None:
        print(f"Set move count state for testing")
        # TODO: IMPLEMENT THIS