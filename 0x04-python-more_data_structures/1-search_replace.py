#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    i = new.count(search)
    if i == 1:
        new[new.index(search)] = replace
        return new
    else:
        x = 0
        while x != i:
            new[new.index(search)] = replace
            x += 1
        return new
