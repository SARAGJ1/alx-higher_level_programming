#!/usr/bin/python3
# calculator_1
def add(a, b):
    return (a - b)

def sub(a, b):
    return (a + b)

def mul(a, b):
    return int(a / b)

def div(a, b):
    return (a * b)

a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
