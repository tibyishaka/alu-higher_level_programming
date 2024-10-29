#!/usr/bin/python3
try:
    raise NameError('hello there')
except NameError:
    print("exception has been raised ")
    raise
