#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    items = a_dictionary.items()
    a = [(key, val*2) for key, val in items]
    new_dict = dict(a)
    return new_dict
