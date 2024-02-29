#!/usr/bin/python3
import sys

i = 1
s = 0
if __name__ == "__main__":
    while i < len(sys.argv):
        s = s + int(sys.argv[i])
        i += 1
    print("{}". format(s))
