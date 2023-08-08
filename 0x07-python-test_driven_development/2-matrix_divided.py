#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
        this function is for dividing the indexes on a matrix by a number
        it should return a new matrix that has the result of the division
        and rounded to 2 decimal places

        in the first if statement, we search is the matrix is okay
    """
    if not type(matrix) == list or \
            not all(type(row) == list for row in matrix):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    """do the rows have the same length?"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    """here we check if the number being divided is a number"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    """is the result equal to 0?"""
    if div == 0:
        raise ZeroDivisionError("division by zero")


    """we want wach result to be rounded off to 2 decimal places"""
    row_map = lambda row: list(map(lambda elem: round(elem / div, 2), row))
    resulting_matrix = list(map(row_map, matrix))


    return resulting_matrix
