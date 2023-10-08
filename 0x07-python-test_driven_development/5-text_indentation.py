#!/usr/bin/python3
"""text_indentation
"""


def text_indentation(text):
    """text_indentation
    arg:
        text: text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newstr = ""
    for i in text:
        if (i == "." or i == "?" or i == ":"):
            newstr += i
            newstr += ("\n" * 2)
        else:
            newstr += i
    print(newstr)
