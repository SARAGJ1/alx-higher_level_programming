#!/usr/bin/python3
"""function that retrieves an element from a list like in C."""


def element_at(my_list, idx):
    """function that retrieves an element from a list like in C."""

    if (idx < 0 or idx >= len(my_list)):
        return None
    else:
        return my_list[idx]
