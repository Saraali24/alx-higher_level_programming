#!/usr/bin/python3
"""models/base.py"""
import json
import os


class Base:
    """Base class of the other shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        json_string = json.dumps(list_dictionaries)
        if list_dictionaries is None:
            return "[]"
        else:
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        filname = f"{cls.__name__}.json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        json_str = cls.to_json_string(new_list)

        with open(filname, "w", encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        new_list = []
        if os.path.isfile(filename):
            with open(filename, "r", encoding='utf-8') as file:
                data = cls.from_json_string(file.read())
            for i in data:
                new_list.append(cls.create(**i))
        return new_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
