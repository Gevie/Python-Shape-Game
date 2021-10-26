from dataclasses import dataclass
from typing import Protocol, Any, Union


class Shape(Protocol):
    """Represents a shape"""
    type: str
    rgb: list
    colour: tuple
    method: str
    positions: dict
    radius: int

    def map(self, position: str) -> Union[list[tuple[Any, Any]], tuple]:
        """Map the shape to the screen"""


@dataclass()
class Rectangle(Shape):
    """Represents a rectangle"""
    type: str
    rgb: list
    colour: tuple
    method: str
    positions: dict

    def map(self, position: str) -> Union[list[tuple[Any, Any]], tuple]:
        """Draw the shape on the screen"""

        rect = (
            self.positions[position][0],
            self.positions[position][1],
            self.positions[position][2],
            self.positions[position][3]
        )

        return rect


@dataclass
class Circle(Shape):
    """Represents a circle"""
    type: str
    rgb: list
    colour: tuple
    method: str
    positions: dict
    radius: int

    def map(self, position: str) -> Union[list[tuple[Any, Any]], tuple]:
        """Draw the shape on the screen"""

        circle = (
            self.positions[position][0],
            self.positions[position][1]
        )

        return circle


@dataclass
class Triangle(Shape):
    """Represents a triangle"""
    type: str
    rgb: list
    colour: tuple
    method: str
    positions: dict

    def map(self, position: str) -> Union[list[tuple[Any, Any]], tuple]:
        """Draw the shape on the screen"""

        polygon = [
            (self.positions[position][0][0], self.positions[position][0][1]),
            (self.positions[position][1][0], self.positions[position][1][1]),
            (self.positions[position][2][0], self.positions[position][2][1]),
        ]

        return polygon


@dataclass
class Parallelogram(Shape):
    """Represents a parallelogram"""
    type: str
    rgb: list
    colour: tuple
    method: str
    positions: dict

    def map(self, position: str) -> Union[list[tuple[Any, Any]], tuple]:
        """Draw the shape on the screen"""

        polygon = [
            (self.positions[position][0][0], self.positions[position][0][1]),
            (self.positions[position][1][0], self.positions[position][1][1]),
            (self.positions[position][2][0], self.positions[position][2][1]),
            (self.positions[position][3][0], self.positions[position][3][1]),
        ]

        return polygon
