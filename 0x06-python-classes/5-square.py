#!/usr/bin/python3
""" Square class """


class Square:
    """Square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise Exception('size must be an integer')
        if value < 0:
            raise Exception('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
        else:
            print()
