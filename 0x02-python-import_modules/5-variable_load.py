#!/usr/bin/python3

if __name__ == "__main__":
    with open("variable_load_5.py") as f:
        code = compile(f.read(), "variable_load_5.py", 'exec')
        exec(code)
    print("{}". format(a))
