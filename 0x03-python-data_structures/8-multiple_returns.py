#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    if sent_len == 0:
        n1 = None
    else:
        n1 = sentence[0]
    return (sent_len, n1)
