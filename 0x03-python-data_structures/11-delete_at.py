#!/usr/bin/python3
"""function that deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """function that deletes the item at a specific position in a list."""

    if (idx < 0 or idx >= len(my_list)):
        return my_list
    new_list = []
    i = 0
    while (i < len(my_list)):
        if (i == idx):
            i = i + 1
        if (i >= len(my_list)):
            return new_list
        new_list.append(my_list[i])
        i = i + 1
    return new_list
