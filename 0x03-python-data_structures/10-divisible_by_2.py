#!/usr/bin/python3
"""function that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list."""

    i = 0
    list_return = []
    while (i < len(my_list)):
        if (my_list[i] % 2 == 0):
            list_return.append(True)
        else:
            list_return.append(False)
        i = i + 1
    return list_return
