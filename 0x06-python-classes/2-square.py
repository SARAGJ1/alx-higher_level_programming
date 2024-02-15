#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class"""

    def __init__(self, size = 0):
        """Initialize Square with optional size"""

        if size < 0:
            print('size must be >= 0')
        if not isinstance(size, int):
            print('size must be an integer')
        self.__size = size
