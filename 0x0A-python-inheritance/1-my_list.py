#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """class MyList that inherits from list"""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        print(sorted(self))
