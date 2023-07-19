#!/usr/bin/python3
def search_replace(my_list, search, replace):
    myNewList = [n for n in my_list]
    for i in range(len(myNewList)):
        if myNewList[i] == search:
            myNewList[i] = replace
    return myNewList
