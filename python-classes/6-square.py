#!/usr/bin/python3
''' coordinates of a square '''


class Square:
    ''' init '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= 0")

        self.__size = size
 
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def position(self):
        return self.__position

    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("Position must be a tuple of 2 positive integer")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = position

    def area(self):
        square_area = self.__size ** 2
        return square_area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[1]):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print()
