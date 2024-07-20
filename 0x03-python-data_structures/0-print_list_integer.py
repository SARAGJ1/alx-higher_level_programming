#!/usr/bin/python3
"""function that prints all integers of a list."""


def print_list_integer(my_list=[]):
    """function that prints all integers of a list."""

    i = 0
    while (i < len(my_list)):
        x = "{:d}".format(my_list[i])
        print(x)
        i = i + 1
