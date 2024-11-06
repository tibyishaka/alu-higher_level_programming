#!/usr/bin/python3
'''class rectangle'''


class Rctangle:
    '''init function'''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(width, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
