#!/usr/bin/python3
"""Module to write"""


def append_write(filename="", text=""):
    """creat the file write in it and read"""

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    j = 0
    for i in text:
        j = j + 1
    return j
