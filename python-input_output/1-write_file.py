#!/usr/bin/python3
''' writing in a file'''


def write_file(filename="", text=""):
    '''function to write text to a file'''
    with open(filename, 'w+') as f:
        return f.write(text)
