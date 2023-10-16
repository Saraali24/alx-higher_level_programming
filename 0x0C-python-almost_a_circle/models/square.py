#!/usr/bin/python3
"""Class that builds a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that build a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of Square"""
        super().__init__(size, size, x, y, id)

    # Getter
    @property
    def size(self):
        """return size"""
        return self.width

    @size.setter
    def size(self, value):
        """checks the size"""
        if not isinstance(value, int):
            TypeError("width must be an integer")
        self.width = value
        self.height = value

    def __str__(self):
        """Override str function to return message"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """Returns the dict representation of a Square"""
        my_dict = {
          'id': self.id,
          'x': self.x,
          'size': self.size,
          'y': self.y
        }
        return my_dict
