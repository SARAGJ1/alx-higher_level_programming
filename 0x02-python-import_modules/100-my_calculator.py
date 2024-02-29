#!/usr/bin/python3
import sys

if __name__ == "__main__":
    with open("calculator_1.py") as f:
        code = compile(f.read(), "calculator_1.py", 'exec')
        exec(code)

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    s = 0
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        s = add(a, b)
    elif sys.argv[2] == "-":
        s = sub(a, b)
    elif sys.argv[2] == "*":
        s = mul(a, b)
    elif sys.argv[2] == "/":
        s = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} ={}". format(sys.argv[1], sys.argv[2], sys.argv[3], s))
