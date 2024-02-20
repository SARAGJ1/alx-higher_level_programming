#!/usr/bin/python3
"""Module to write"""


def write_file(filename="", text=""):
    """creat the file write in it and read"""

    with open(filename, 'w') as f:
        for text in open(filename):
            print(text, end="")

    with open(filename,'w', encoding="utf-8") as f:
        return f.write(text)
