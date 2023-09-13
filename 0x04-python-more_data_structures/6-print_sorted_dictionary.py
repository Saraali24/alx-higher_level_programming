#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = sorted(a_dictionary.items())
    for key, val in s:
        print(f"{key}: {val}")
