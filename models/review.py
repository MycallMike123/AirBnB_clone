#!/usr/bin/python3
"""A Module that defines the state model"""

from .base_model import BaseModel


class Review(BaseModel):
    """A class with the blueprint for Review objects"""
    user_id = ""
    place_id = ""
    text = ""
