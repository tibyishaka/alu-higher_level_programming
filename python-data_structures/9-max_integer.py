#!/usr/bin/python3
def max_integer(my_list):
    if not my_list:
        return None
    else:
         if len(my_list) == 1:
            return my_list[0]
         else:
            i = my_list[0]
            j = max_integer(my_list[1:])
            if i > j:
                return i
            else:
                return j
