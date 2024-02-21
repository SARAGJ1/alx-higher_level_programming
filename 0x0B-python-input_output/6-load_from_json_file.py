#!/usr/bin/python3
"""json file"""
import json


def load_from_json_file(filename):
    """json"""

    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
        return json_data
