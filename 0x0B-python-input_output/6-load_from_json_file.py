#!/usr/bin/python3
"""json file"""
import json


def load_from_json_file(filename):
    """json"""

    file_path = 'filename.json'

    with open(file_path, 'w') as json_file:
        json.dump(filename)
