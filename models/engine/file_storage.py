#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file"""

import json
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""

        with open(FileStorage.__file_path, 'w+') as f:
            dictofobjs = {}

            for key, value in FileStorage.__objects.items():
                dictofobjs[key] = value.to_dict()

            json.dump(dictofobjs, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())

                from models.base_model import BaseModel
                from models.user import User

                for key, value in dictofobjs.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)

                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)

                    elif value['__class__'] == 'Place':
                        FileStorage.__objects[key] = Place(**value)

                    elif value['__class__'] == 'State':
                        FileStorage.__objects[key] = State(**value)

                    elif value['__class__'] == 'City':
                        FileStorage.__objects[key] = City(**value)

                    elif value['__class__'] == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)

                    elif value['__class__'] == 'Review':
                        FileStorage.__objects[key] = Review(**value)

        except FileNotFoundError:
            pass
