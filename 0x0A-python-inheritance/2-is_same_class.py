#!/usr/bin/python3
"""module for is_same_class method."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""
    return type(obj) == a_class
