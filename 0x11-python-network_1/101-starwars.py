#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API."""

import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    count = results.get("count")
    print("Number of results: {}".format(count))

    j = 0
    while j < count:
        for r in results.get("results"):
            print(x.get("name"))
            j += 1
        next_page = results.get("next")
        if next_page is not None:
                results = requests.get(next_page).json()
