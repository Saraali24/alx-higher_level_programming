#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(id=89,width=2, x=3, y=1)
    print(r1)

    r1.update(width=4, x=1, height=2, y=3 )
    print(r1)
