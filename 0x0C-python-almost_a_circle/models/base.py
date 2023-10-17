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
        """Returns JSON string representation"""
        if list_dictionaries == [] or list_dictionaries is None:
            return list_dictionaries == []
        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string repr to file"""
        if list_objs is None:
            return list_objs == []
        else:
            json_string = \
                Base.to_json_string([obj.to_dictionary() for obj in list_objs])
            filename = Base.__name__ + ".json"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(json_string)
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
