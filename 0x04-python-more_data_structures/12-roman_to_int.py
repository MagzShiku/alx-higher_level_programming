#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    numbering_system = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000
    }

    digit = list(map(numbering_system.get, roman_string))
    combination = zip(digit, digit[1:])
    out_come = (sum(-a if a < b else a for a, b in combination) + digit[-1])

    return (out_come)
