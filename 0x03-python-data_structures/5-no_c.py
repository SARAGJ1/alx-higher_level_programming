#!/usr/bin/python3
"""function that removes all characters c and C from a string."""


def no_c(my_string):
    """function that removes all characters c and C from a string."""

    new_string = []
         
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string.append(char)

    return ''.join(new_string)
