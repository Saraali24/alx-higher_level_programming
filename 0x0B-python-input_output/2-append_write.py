#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
        Args:
            filename (str): The name of the file to append to.
            text (str): The string to append to the file.
        Returns:
            The number of characters appended.
    """
    with open('file_append.txt', 'a', encoding='UTF8') as filename:
        filename.write(text)
        return len(text)
