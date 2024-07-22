#!/usr/bin/python3
"""replaces an element in a list without modifying the original list"""


def new_in_list(my_list, idx, element):
    """replaces an element in a list without modifying the original list"""

    new_list = my_list[:]
    if (idx < 0 or idx >= len(my_list)):
        return my_list
    else:
        new_list[idx] = element
        return new_list
