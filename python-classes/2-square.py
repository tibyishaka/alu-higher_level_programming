#!/usr/bin/python3
''' creating a python class  and size validation with class '''


class Square:
    ''' creating a square class with a private size attribute'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
