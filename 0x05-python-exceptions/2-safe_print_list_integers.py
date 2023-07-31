#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    i = 0

    try:
        while elements < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                elements += 1
                if elements < x:
                    print(" ", end="")
            i += 1
    except IndexError:
        pass
    finally:
        print()
    return elements
