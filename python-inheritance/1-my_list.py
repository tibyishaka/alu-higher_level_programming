#!/usr/bin/python3
'''print sorted list'''


class Mylist(list):
    '''
    function 
    to
    print
    '''

    def print_sorted(self):
        ''' sorting the list '''
        sorted_list = self[:]
        sorted_list.sort()
        print( "{}".format(sorted_list))
