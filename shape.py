from dataclasses import dataclass
from typing import Protocol


class Shape(Protocol):
    """Represents a shape"""
    method: str

    def draw(self, position: str) -> list:
        """Draw the shape on the screen"""


@dataclass()
class Rectangle(Shape):
    """Represents a rectangle"""
    type: str
    colour: list
    method: str
    positions: dict

    def draw(self, position: str) -> list:
        """Draw the shape on the screen"""

        colour = (self.colour[0], self.colour[1], self.colour[2])
        rect = (
            self.positions[position][0],
            self.positions[position][1],
            self.positions[position][2],
            self.positions[position][3]
        )

        return [colour, rect]


@dataclass
class Circle(Shape):
    """Represents a circle"""
    type: str
    colour: list
    method: str
    positions: dict
    radius: int

    def draw(self, position: str) -> list:
        """Draw the shape on the screen"""

        colour = (self.colour[0], self.colour[1], self.colour[2])
        circle = (
            self.positions[position][0],
            self.positions[position][1]
        )

        return [colour, circle, self.radius]


@dataclass
class Triangle(Shape):
    """Represents a triangle"""
    type: str
    colour: list
    method: str
    positions: dict

    def draw(self, position: str) -> list:
        """Draw the shape on the screen"""

        colour = (self.colour[0], self.colour[1], self.colour[2])
        polygon = [
            (self.positions[position][0][0], self.positions[position][0][1]),
            (self.positions[position][1][0], self.positions[position][1][1]),
            (self.positions[position][2][0], self.positions[position][2][1]),
        ]

        return [colour, polygon]


@dataclass
class Parallelogram(Shape):
    """Represents a parallelogram"""
    type: str
    colour: list
    method: str
    positions: dict

    def draw(self, position: str) -> list:
        """Draw the shape on the screen"""

        colour = (self.colour[0], self.colour[1], self.colour[2])
        polygon = [
            (self.positions[position][0][0], self.positions[position][0][1]),
            (self.positions[position][1][0], self.positions[position][1][1]),
            (self.positions[position][2][0], self.positions[position][2][1]),
            (self.positions[position][3][0], self.positions[position][3][1]),
        ]

        return [colour, polygon]
