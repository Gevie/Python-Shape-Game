from typing import Callable, Any

from shape import Shape

shape_creation_functions: dict[str, Callable[..., Shape]] = {}


def register(shape_type: str, creation_function: Callable[..., Shape]):
    """Register a new shape"""
    shape_creation_functions[shape_type] = creation_function


def unregister(shape_type: str):
    """Unregister a shape"""
    shape_creation_functions.pop(shape_type, None)


def create(arguments: dict[str, Any]) -> Shape:
    """Create a shape of a specific type, given arguments"""
    arguments_copy = arguments.copy()
    shape_type = arguments_copy.pop('type')

    rgb = arguments_copy.pop('rgb')
    arguments['colour'] = (rgb[0], rgb[1], rgb[2])

    print(arguments)

    try:
        creation_function = shape_creation_functions[shape_type]
        return creation_function(**arguments)
    except KeyError:
        raise ValueError(f"Unknown shape type {shape_type}") from None
