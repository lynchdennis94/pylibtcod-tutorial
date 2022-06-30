from typing import Tuple


class Entity:
    """Class to represent a generic entity within the game"""

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        """Moves the entity by the dx and dy amounts"""
        self.x += dx
        self.y += dy
