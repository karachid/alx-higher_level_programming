#!/usr/bin/python3
"""
Defines the class BaseGeometry
"""


class BaseGeometry:
    """Class with public attribute area"""
    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")
