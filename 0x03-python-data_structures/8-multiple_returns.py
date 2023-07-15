#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        n1 = None
    else:
        n1 = sentence[0]
    return (l, n1)
