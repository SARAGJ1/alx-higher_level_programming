#!/usr/bin/python3
"""function that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""

    if (my_list is not None):
        i = len(my_list)
        while (i > 0):
            x = "{:d}".format(my_list[i - 1])
            print(x)
            i = i - 1
