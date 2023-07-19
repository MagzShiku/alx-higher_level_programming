#!/usr/bin/python3
def best_score(a_dictionary):
    if not bool(a_dictionary):
        return None

    # the above checks if there is anything in the dictionary

    highest_value = max(a_dictionary.values())
    n = list(a_dictionary.keys())

    i = 0
    while i < len(n):
        if a_dictionary[n[i]] == highest_value:
            return (n[i])
        i += 1

