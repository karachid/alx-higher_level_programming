#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dict = a_dictionary.copy()
    l_keys = list(n_dict)

    for i in l_keys:
        n_dict[i] *= 2

    return (n_dict)
