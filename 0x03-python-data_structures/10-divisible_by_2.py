#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _output = []
    for _int in my_list:
        if _int % 2 == 0:
            _output.append(True)
        else:
            _output.append(False)
    return (_output)
