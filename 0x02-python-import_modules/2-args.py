#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_args = len(sys.argv) - 1

    if total_args == 0:
        print("{} arguments.".format(total_args))
    elif total_args == 1:
        print("{} argument:".format(total_args))
    else:   
        print("{} arguments:".format(total_args))

    for i in range(total_args):
        print("{}: {}".format(i+1, sys.argv[i+1]))
