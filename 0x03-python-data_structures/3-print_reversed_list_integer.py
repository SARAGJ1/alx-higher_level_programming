#!/usr/bin/python3
"""function that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""

    i = len(my_list)
    while (i > len(my_list)):
        x = "{:d}".format(my_list[i])
        print(x)
        i = i - 1
