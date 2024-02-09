#!/usr/bin/python3

"""Defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributs/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""

        if kwargs is not None and len(kwargs) != 0:

            if '__class__' in kwargs:
                del kwargs['__class__']

            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """String representation of BaseModel instance"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attr updated_at with the datetime"""
        self.__dict__.update({'updated_at': datetime.now()})
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of instances"""

        new_dict = dict(self.__dict__)
        new_dict.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                         'id': self.id,
                         'created_at': self.created_at.isoformat()})
        return new_dict
