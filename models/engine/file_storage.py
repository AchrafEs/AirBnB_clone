#!/usr/bin/python3
""" This module is composed of FileStorage class."""
import json


class FileStorage:
    """ A class that serializes instances to a
        JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Initializes FileStorage instance.

            Private attributes:
                __file_path (string): stores the path to JSON file.
                __objects (dict): stores class objects."""

    def all(self):
        """ Returns the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
