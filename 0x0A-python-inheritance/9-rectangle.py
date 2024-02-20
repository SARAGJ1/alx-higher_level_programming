#!/usr/bin/python3
"""not empty class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherit from basegeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
        return str(self.__width*self.__height)
