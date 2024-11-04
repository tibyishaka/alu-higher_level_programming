#!/usr/bin/python3
''' printing a class'''


class Square:
    ''' init function '''
    def __init__(self, size=0):
        self.__size = size
       
    def size(self):
        return self.__size
    
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        s_area = self.__size ** 2
        return s_area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
