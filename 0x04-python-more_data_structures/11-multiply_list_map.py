#!/usr/bin/python3
"""returns a list with all values * by a number without using any loops."""


def multiply_list_map(my_list=[], number=0):
    """returns a list with all values * by a number without using any loops."""

    def multi(x):
        return x * number
    
    y = list(map(multi, my_list))
    return y
