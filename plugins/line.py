from dataclasses import dataclass
from typing import Any, Union
import factory
from shape import Shape


@dataclass()
class Line(Shape):
    """Represents a line"""
    type: str
    rgb: list
    colour: tuple
    method: str
    positions: dict
    radius: int

    def map(self, position: str) -> Union[list[tuple[Any, Any]], tuple]:
        """Draw the shape on the screen"""

        line = [
            (self.positions[position][0][0], self.positions[position][0][1]),
            (self.positions[position][1][0], self.positions[position][1][1])
        ]

        return line


def initialize() -> None:
    factory.register('line', Line)

