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
    
    @staticmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON of a list of objects to a file
        Args:
            list_objs (list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

