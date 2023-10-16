#!/usr/bin/python3
"""Defines a Base base class"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON of a list of dicts
        Args:
            list_dictionaries (list): List of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
