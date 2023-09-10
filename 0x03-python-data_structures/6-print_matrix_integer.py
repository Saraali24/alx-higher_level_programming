#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a in row:
            if a == row[-1]:
                print("{:d}".format(a), end='')
            else:
                print("{:d}".format(a), end=' ')
        print()
