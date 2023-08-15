#!/usr/bin/python3

"""
this function returns a lst of integers representing pascal's triangle
returns empty lst if n<= 0
we assume n will always be an integer
"""


def pascal_triangle(n):
    """returns integers in pascal's triangle"""
    if n <= 0:
        return []
    # returns empty lst if lst is < 0

    shape = [[1]]
    # initialize variable shape to take integers in the triangle

    for row in range(1, n):
        latd = [1]

        for col in range(1, row):
            latd.append(shape[row - 1][col - 1] + shape[row - 1][col])

        latd.append(1)
        shape.append(latd)

    return shape
