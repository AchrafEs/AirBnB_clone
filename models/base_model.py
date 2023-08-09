#!/usr/bin/python3
""" This module is composed of BaseModel class."""
import datetime
import uuid


class BaseModel:
    """ Defines all common attributes/methods for other classes."""

    def __init__(self, id=str(uuid.uuid4()),
                 created_at=datetime.datetime.now(),
                 updated_at=datetime.datetime.now()):
        """ Initializes a BaseModel object.

            Params:
                id (string): initialized with uuid string
                        when an instance is created.
                created_at (datetime): assigned with the current datetime
                                when an instance is created.
                updated_at (datetime): assigned and updated
                                when an instance is created or changed."""
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance. """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
