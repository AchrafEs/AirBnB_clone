#!/usr/bin/python3
'''Inherent of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''amenity class'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
