#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_sort = sorted(a_dictionary.items(), key=lambda x: x[1])
        return list_sort[-1][0]
    else:
        return None
