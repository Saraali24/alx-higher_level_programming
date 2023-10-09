#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """ MyList class"""

    def print_sorted(self):
        """print_sorted function"""

        new_list = sorted(self)
        print(new_list)
