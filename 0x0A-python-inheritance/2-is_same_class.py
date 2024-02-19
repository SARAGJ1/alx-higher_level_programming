#!/usr/bin/python3
"""the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """func that check if the object is of a_class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if type(obj) == a_class:
        return True
    return False
