#!/usr/bin/python3
"""Module to write"""


def append_write(filename="", text=""):
    """creat the file write in it and read"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()

    with open(filename, 'w', encoding="utf-8") as f:
        append_data = read_data + text
        f.write(append_data)
        return f.write(text)
