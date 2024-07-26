#!/usr/bin/python3
"""replaces all occurrences of an element by another in a new list."""


def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""

    new = [replace if element == search else element for element in my_list]
    return new
