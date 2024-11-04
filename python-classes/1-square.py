#!/usr/bin/python3
''' careatig aclass with a private attribute'''

class Square:
    '''creating class with private size attribute'''
    def __init__(self, size):
        '''initialising size'''
        self.__size = size
