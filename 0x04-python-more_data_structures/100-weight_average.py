#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    res = [a * b for a, b in my_list] # a & b represent score and weight
    return (sum(res) / sum(b for a, b in my_list))
