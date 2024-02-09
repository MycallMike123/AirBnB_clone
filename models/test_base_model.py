#!/usr/bin/python3
"""A module that tests base_model"""

from datetime import datetime
import unittest
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """A class with the test cases for the base_model"""

    def test_str(self):
        """function that checks the str output of an instance"""

        base = BaseModel()
        self.assertEqual(base.__str__(),
                         f"[{type(base).__name__}] \
({base.id}) {base.__dict__}")

    def test_to_dict(self):
        """function that checks the to_dict() function of an instance"""

        base = BaseModel()
        prev_time = base.updated_at
        self.assertDictEqual(base.to_dict(),
                             {'__class__': type(base).__name__,
                              'updated_at': base.updated_at.isoformat(),
                              'id': base.id,
                              'created_at': base.created_at.isoformat()})
        base.save()
        self.assertNotEqual(prev_time, base.updated_at)

    def test_attr_classes(self):
        """
        checks if the right classes were use to generate attributes
        """
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)

    def test_save(self):
        """
        tests the save method
        """
        base = BaseModel()
        prevtime = base.updated_at
        base.save()
        newtime = base.updated_at
        self.assertNotEqual(prevtime, newtime)
