#!/usr/bin/python3
"""Module that reads a files"""


def read_file(filename=""):
    """read only"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
