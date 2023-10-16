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
    
    @classmethod
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

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialization of a JSON string
        Args:
            json_string (str): A JSON str of a list of dict
        Returns:
            If json_string is None or empty - an empty list
            Otherwise - the Python list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantied from a dict of atts
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
