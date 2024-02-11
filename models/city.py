#!/usr/bin/python3
"""A module thatDefines the state model"""

from .base_model import BaseModel


class City(BaseModel):
    """A class with the blueprint for City objects"""

    state_id = ""
    name = ""
