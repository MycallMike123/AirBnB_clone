#!/usr/bin/python3
"""A module that tests for base_model"""

import unittest
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel


class Teststorage(unittest.TestCase):
    def test_init(self):
        base = BaseModel()
        self.assertEqual(base.__class__, BaseModel)
        self.assertIsInstance(storage, FileStorage)
