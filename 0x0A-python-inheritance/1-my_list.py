#!/usr/bin/python3
class MyList(list):
    """ MyList class"""

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
