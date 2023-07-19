#!/usr/bin/python3
def uniq_add(my_list=[]):
    ints_in_list = set()
    idx = 0
    while idx < len(my_list):
        if my_list[idx] not in ints_in_list:
            ints_in_list.add(my_list[idx])
        idx += 1
    return sum(ints_in_list)
