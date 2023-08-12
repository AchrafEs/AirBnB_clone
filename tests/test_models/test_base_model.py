#!/usr/bin/python3
""" This module implements Unit Tests for Base class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime as dt


class TestBaseModel(unittest.TestCase):
    """ Unit Test class for BaseModel class."""
    pass
    # def test_BaseModel_init(self):
    #     model = BaseModel()
    #     self.assertEqual(type(model.id), type(""))
    #     self.assertEqual(type(model.created_at), type(dt.now()))
    #     self.assertEqual(type(model.updated_at), type(dt.now()))

    # def test_to_dict(self):
    #     model = BaseModel()
    #     self.assertEqual(type(model.to_dict()), type({}))


if __name__ == '__main__':
    unittest.main()
