#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        for i in my_list:
            maxnum = max_integer(my_list=[i])
        return maxnum
    else:
        return None
