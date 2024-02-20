#!/usr/bin/python3
"""not empty class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherit from rectagle"""

    def __init__(self, size):
        """Intialize a new Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
