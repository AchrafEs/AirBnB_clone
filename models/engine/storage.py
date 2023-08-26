#!/usr/bin/python3
""" This module is composed of FileStorage class."""
import json
import os


class FileStorage:
    """ A class that serializes instances to a
        JSON file and deserializes JSON file to instances.

        Attributes:
            __file_path (string): stores the path to JSON file.
            __objects (dict): stores class objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects."""

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as f:
                    FileStorage.__objects = json.load(f)
            except Exception with e:
                print("Error loading JSON file:", str(e))
        else:
            print("JSON file does not exist.")
