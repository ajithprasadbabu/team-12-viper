from dataclasses import dataclass


@dataclass
class Character:
    name: str
    DEFAULT_CHAR_NAME = "Viper"
    def __init__(self, name=DEFAULT_CHAR_NAME):
        self.name = name
        self.cPos = None
