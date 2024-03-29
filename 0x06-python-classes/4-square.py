#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class"""

    def __init__(self, size=0):
        """Initialize Square with optional size"""

        self.size = size

    def size(self):
        """get size"""

        return (self.__size)

    def size(self, value):
        """check size"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area"""

        return (self.size*self.size)
