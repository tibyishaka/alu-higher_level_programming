#!/usr/bin/python3
''' number of instances '''


class Rectangle:
    '''def initi '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
         return self.__width

    def width(self, value):
         if not isinstance(width, int):
             raise TypeError("width must be an integer")
         if width < 0:
             raise ValueError("width must be >= 0")
         self.__width = width

    def height(self):
          if not isinstance(height, int):
              raise TypeError("height must be an integer")
          if height < 0:
              raise ValueError("height must be >= 0")
          self.__height = height

    def area(self):
          return self.__width * self.__height


    def perimeter(self):
        if self.__width == 0 or self.__height == 0 :
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle ...")

    def __str__(self):
         if self.__width == 0 or self.__height == 0:
             return ''
         else:
             R = ''
             for i in range(self.__height):
                 for j in range(self.__width):
                     R = R + '#'
                 R += '\n'
             return R[:-1]

    def __repr__(self):
         return "Rectangle({}, {})".format(self.__width, self.__height)
