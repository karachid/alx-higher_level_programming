#!/usr/bin/python3
"""
Defines the lookup function
"""


def lookup(obj):
    """returns a list of methods and attributes of a given object"""
    return dir(obj)
