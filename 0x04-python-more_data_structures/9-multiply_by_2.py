#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    idx = list(a_dictionary.keys())

    i = 0
    while i < len(idx):
        new_dict[idx[i]] = a_dictionary[idx[i]] * 2
        i += 1

    return (new_dict)
