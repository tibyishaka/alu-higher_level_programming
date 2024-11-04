#!/usr/bin/python3
'''getter and setter '''


class Square:
    '''init function '''
    def __init__(self, size=0):
        self.__size = size


    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def area(self):
        s_area = self.size ** 2
        return s_area
