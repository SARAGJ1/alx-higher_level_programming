#!/usr/bin/python3
"""Area of Square Module"""
class Square:
        """ Square Class"""

        def __init__(self, size=0):
        """Initialize Square with optional size"""

            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            self.__size = size

        def area(self):
        """Area"""

            return size*size
