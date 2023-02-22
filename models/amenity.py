#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{Amenity.__name__}] ({self.id}) {self.__dict__}"
