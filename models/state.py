#!/usr/bin/pyhon3
'''Inherent of BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''state class'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)