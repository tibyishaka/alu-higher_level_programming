#!/usr/bin/python3
''' finding the area of square'''


class Square:
    '''init '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    ''' def of finding area'''
    def area(self):
        square_area = self.__size ** 2
        return square_area
