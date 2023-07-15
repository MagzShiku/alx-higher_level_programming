#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for  the_row in matrix:
        for row_val in the_row:
            print(f"{row_val:d}", end="")
            if row_val != the_row[- 1]:
                print(" ", end="")
        print("")
