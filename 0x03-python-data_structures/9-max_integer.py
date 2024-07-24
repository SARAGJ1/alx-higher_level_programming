#!/usr/bin/python3
"""function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """function that finds the biggest integer of a list."""

    x = 0
    i = 0
    while (i < len(my_list)):
        if (x < my_list[i]):
            x = my_list[i]
        i = i + 1
    return x
