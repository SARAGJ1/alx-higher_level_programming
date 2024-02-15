#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class"""

    def __init__(self, value):
        """Initialize Square with optional size"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def size(self):
        """get size"""

        return self.__size

    def __init__(self, size=0):
        """initialisation"""

        self.__size = size

    def area(self):
        """area"""

        return self.__size*self.__size
