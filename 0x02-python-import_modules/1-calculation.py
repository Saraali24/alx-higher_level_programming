#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    e = add(a, b)
    s = sub(a, b)
    x = mul(a, b)
    d = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, e))
    print("{:d} - {:d} = {:d}".format(a, b, s))
    print("{:d} * {:d} = {:d}".format(a, b, x))
    print("{:d} / {:d} = {:d}".format(a, b, d))
