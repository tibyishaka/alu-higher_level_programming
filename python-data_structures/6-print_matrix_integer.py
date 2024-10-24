#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print()
        else:
            for n in i:
                if n == i[-1]:
                    print('{:d}'.format(n))
                else:
                    print('{:d}'.format(n), end=" ")
