#!/usr/bin/python3
"""Module to write"""


def append_write(filename="", text=""):
    """creat the file write in it and read"""

    with open(filename, 'r+', encoding="utf-8") as f:
        read_data = f.read()
        append_data = read_data + text
        f.write(append_data)

    j = 0
    for i in text:
        j = j + 1
    return j
