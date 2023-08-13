#!/usr/bin/python3
""" This module is composed of FileStorage class."""
import json


class FileStorage:
    """ A class that serializes instances to a
        JSON file and deserializes JSON file to instances."""

    def __init__(self, file_path="file.json", objects={}):
        """ Initializes FileStorage instance.

            Private attributes:
                __file_path (string): stores the path to JSON file.
                __objects (dict): stores class objects."""
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """ Returns the __objects dictionary."""
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
