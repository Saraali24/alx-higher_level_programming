#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        x = len(sentence)
        char1 = sentence[0]
        return (x, char1)
    else:
        return (0, None)
