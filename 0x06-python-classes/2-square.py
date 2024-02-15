#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class"""

    def __init__(self, _Square__size):
        self._Square__size = _Square__size
        if _Square__size < 0:
            print('size must be >= 0')
        if type(_Square__size) != int:
            print('size must be an integer')
