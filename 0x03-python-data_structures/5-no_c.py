#!/usr/bin/python3

def no_c(my_string):
    n_string = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            n_string = n_string+c
    return n_string
