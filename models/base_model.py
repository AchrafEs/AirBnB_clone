#!/usr/bin/python3
""" This module is composed of BaseModel class."""
from datetime import datetime as dt
from uuid import uuid4


class BaseModel:
    """ Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """ Initializes a BaseModel object.

            Params:
                args (list): empty.
                kwargs (dict): holds and entire object info."""
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if kwargs == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    self.__setattr__(key, dt.fromisoformat(val))
                else:
                    self.__setattr__(key, val)
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime."""
        self.updated_at = dt.now()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance. """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.__dict__['created_at'].\
            isoformat()
        self.__dict__['updated_at'] = self.__dict__['updated_at'].\
            isoformat()
        return self.__dict__
