#!/usr/bin/python3
"""returns a key with the biggest integer value."""


def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

    x = 0
    if a_dictionary == None:
        return None

    for value in a_dictionary.values():
        if x < value:
            x = value

    for key, value in a_dictionary.items():
        if value == x:
            return key
