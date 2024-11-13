#!/usr/bin/python3
'''function that writes an Object to a text file'''


import json


def save_to_json_file(my_obj, filename):
    '''f unction that writes object'''
    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
