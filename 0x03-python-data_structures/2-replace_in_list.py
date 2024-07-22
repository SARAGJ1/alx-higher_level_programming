#!/usr/bin/python3
"""function that replaces an element of a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position."""

    if (idx < 0 or idx >= len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
