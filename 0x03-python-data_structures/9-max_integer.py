#!/usr/bin/python3

def max_integer(my_list=[]):
    n_max
    if len(my_list) == 0:
        return "None"
    else:
        n_max = my_list[0]
        for i in range(1, len(my_list)):
            if n_max < my_list[i]:
                n_max = my_list[i]
        return n_max
