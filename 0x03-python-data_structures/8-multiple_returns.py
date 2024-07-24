#!/usr/bin/python3
"""returns tuple with the length of a string and its first character."""


def multiple_returns(sentence):
    """returns tuple with the length of a string and its first character."""

    if len(sentence) == 0:
        tuple_a = (0, None)
    else:
        tuple_a = (len(sentence), sentence[0])
    return tuple_a
