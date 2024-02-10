#!/usr/bin/python3
"""Module for Airbnb Console"""
import cmd
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The entry point for the command interpreter"""

    prompt = '(hbnb) '

    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

    dotcmds = ['.all()', '.count()']

    def do_create(self, line):
        """Creates a new instance of a given class, saves it \
(to the JSON file) and prints the id."""

        if line == '':
            print('** class name missing **')

        elif line not in AirBnbCmd.models:
            print('** class doesn\'t exist **')

        else:
            if line == 'BaseModel':
                instance = BaseModel()

            elif line == 'User':
                instance = User()

            elif line == 'Place':
                instance = Place()

            elif line == 'State':
                instance = State()

            elif line == 'City':
                instance = City()

            elif line == 'Amenity':
                instance = Amenity()

            elif line == 'Review':
                instance = Review()

            storage.save()
            print(instance.id)
