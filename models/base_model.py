#!/usr/bin/python3
""" This module is composed of BaseModel class."""
from datetime import datetime as dt
from uuid import uuid4


class BaseModel:
    """ Defines all common attributes/methods for other classes."""

    def __init__(self,
                 id=str(uuid4()),
                 created_at=dt.now(),
                 updated_at=dt.now()):
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
        return (f"['BaseModel'] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime."""
        self.updated_at = dt.now()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance. """
        self.__dict__["__class__"] = "BaseModel"
        self.__dict__["created_at"] = self.__dict__["created_at"].\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["updated_at"] = self.__dict__["updated_at"].\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__
