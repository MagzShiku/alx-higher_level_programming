#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.keys())
    for n in new_dict:

        idx = a_dictionary[n]
        print("{}: {}".format(n, idx))
        # print out the value of keys, orderd
