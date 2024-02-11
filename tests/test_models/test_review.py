#!/usr/bin/python3
"""A module that Tests suite for base_model"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_parent(self):
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))
