#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """inherits_from function"""
    obj_class = obj.__class__
    return issubclass(obj_class, a_class) and obj_class != a_class
