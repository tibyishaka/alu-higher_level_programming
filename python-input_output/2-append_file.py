#!/usr/bin/python3
'''' appending string to the end of file'''


def append_write(filename=" ", text=""):
    '''function to append string to file'''
    with open(filename,'a+') as f :
        return f.write(text)
