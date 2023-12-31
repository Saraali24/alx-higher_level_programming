#!/usr/bin/python3
"""matrix_divided function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

        Args:
            matrix (list): A list of lists of ints or floats.
            div (int/float): The divisor.
        Raises:
            TypeError: If the matrix contains non-numbers.
            TypeError: If the matrix contains rows of different sizes.
            TypeError: If div is not an int or float.
            ZeroDivisionError: If div is 0.
        Returns:
            A new matrix representing the result of the division.

    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of\
                         integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of\
                         integers/floats")
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must \
                            have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    n = [[(round((num / div), 2)) for num in row] for row in matrix]
    return (n)
