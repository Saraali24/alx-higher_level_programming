#!/usr/bin/python3
"""read function"""


def read_file(filename=""):
    with open('my_file_0.txt', encoding='UTF8') as filename:
        x = filename.read()
        print(x)
