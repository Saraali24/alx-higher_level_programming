#!/usr/bin/python3
"""class"""
from models.base import Base


class Rectangle(Base):
    """Build a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Checks x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Checks y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Print the shape with character '#'"""
        for a in range(self.__y):
            print("")
        for b in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Override str function to return message"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width,
                self.height))

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dict representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
            }
