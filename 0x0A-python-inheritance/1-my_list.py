#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def __init__(self, *args):
    """func that inherits"""

        super().__init__(*args)

    def print_sorted(self):
    """func that organize the list"""

        print_sorted = sorted(self)
        print(print_sorted)
