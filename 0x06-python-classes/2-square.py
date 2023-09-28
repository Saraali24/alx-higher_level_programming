#!/usr/bin/python3
""" Square class """


class Square:
    """Square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise Exception('size must be an integer')
        elif size < 0:
            raise Exception('size must be >= 0')

        self._Square__size = size
