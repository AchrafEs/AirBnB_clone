#!/usr/bin/python3
"""file_storage.py module"""
import json
import os

# from models.user import User
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State


class FileStorage():
    """
    FileStorage class:
    ------------------
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        public instance method that serializes __objects
        to the JSON file (path: __file_path).
        Variables:
        ----------
        new_dict [dict] -- keys and values to build JSON.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        from models.base_model import BaseModel

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                s_obj = json.load(file)

                for key, val in s_obj.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        self.new(BaseModel(**val))
