#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new = set(my_list)
    for i in new:
        result = result + i
    return result
