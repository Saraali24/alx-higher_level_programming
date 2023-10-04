#!/usr/bin/python3
"""class called Rectangle"""


class Rectangle:
    """a Rectangle
    width is a Private instance attribute
    height is a Private instance attribute
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__height + self.__width) * 2)

    def __str__(self):

        s = ""
        if self.__height == 0 or self.__width == 0:
            return s

        for i in range(0, self.__height):
            for j in range(0, self.__width):
                s += '#'
            if i == self.__height - 1:
                pass
            else:
                s += '\n'
        return s

    def __repr__(self):

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
