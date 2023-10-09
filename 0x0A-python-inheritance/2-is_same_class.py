#!/usr/bin/python3
"""
Contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """Returns true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
