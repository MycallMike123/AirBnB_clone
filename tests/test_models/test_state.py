#!/usr/bin/python3
"""A module that test suite for base_model"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_attr(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_parent(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
