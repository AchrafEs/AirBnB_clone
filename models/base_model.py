#!/usr/bin/python3
""" This module is composed of BaseModel class."""
from datetime import datetime as dt
from uuid import uuid4
from . import storage


class BaseModel:
    """ Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """ Initializes a BaseModel object.

            Params:
                args (tuple): empty
                kwargs (dict): passes all instance attributes.

            Public attributes:
                id (string): initialized with uuid string
                        when an instance is created.
                created_at (datetime): assigned with the current datetime
                                when an instance is created.
                updated_at (datetime): assigned and updated
                                when an instance is created or changed."""
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    self.__setattr__(key, dt.fromisoformat(val))
                else:
                    self.__setattr__(key, val)
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime."""
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance. """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
