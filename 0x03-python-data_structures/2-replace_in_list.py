#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx >=len(my_list):
        return None
    else:
        return my_list[idx]
