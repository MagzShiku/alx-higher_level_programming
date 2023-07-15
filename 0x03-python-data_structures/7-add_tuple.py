#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp_a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    tp_a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tp_b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tp_b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (tp_a1 + tp_b1, tp_a2 + tp_b2)
