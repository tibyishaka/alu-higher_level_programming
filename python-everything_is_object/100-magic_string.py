#!/usr/bin/python3
def magix_string():
     magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Holberton, " * (magic_string.n - 1) + "Holberton")

