#!/usr/bin/python3
import sys

i = 1
if __name__ == "__main__":
    print("{} argument:". format(len(sys.argv) - 1))
    while i < len(sys.argv):
        print("{}: {}". format(i, sys.argv[i]))
        i += 1
