#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary)

    for val_dic in list_keys:
        if value == a_dictionary.get(val_dic):
            del a_dictionary[val_dic]

    return (a_dictionary)
