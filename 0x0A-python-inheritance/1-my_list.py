#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
"""Implements sorted printing for the built-in list class."""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
     """Print a list in sorted ascending order."""
        print(sorted(self))
