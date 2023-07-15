#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest_val = my_list[0]
    for i in my_list:
        if i > largest_val:
            largest_val = i
    return largest_val
