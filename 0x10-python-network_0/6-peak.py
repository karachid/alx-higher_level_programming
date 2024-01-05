#!/usr/bin/python3
""" Defines the find_peak function """


def find_peak(list_of_integers):
    """ Function that implements find_peak in a list """
    if list_of_integers is None or not list_of_integers:
        return None
    return max(list_of_integers)
