#!/usr/bin/python3
"""json file"""


import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """func main"""

    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
        k = my_list + sys.argv[1:]
        save_to_json_file(k, filename)
