#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        argv_list = sys.argv
        a = int(argv_list[1])
        operator = argv_list[2]
        b = int(argv_list[3])
        if operator == '+':
            print(f"{a} + {b} = {add(a, b)}")
        elif operator == '-':
            print(f"{a} - {b} = {sub(a, b)}")
        elif operator == '*':
            print(f"{a} * {b} = {mul(a, b)}")
        elif operator == '/':
            print(f"{a} / {b} = {div(a, b)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
