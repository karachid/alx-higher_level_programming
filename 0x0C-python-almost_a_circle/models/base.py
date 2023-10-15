#!/usr/bin/python3
"""Defines a Base base class"""

class Base:
    """Declares the Base class
    Acts as the "base" for all other classes in the project
    Attributes:
        __nb_objects (int): Number of instantiated objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new instance 
        
        Args:
            id (int): Id Id of the new instance.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
