#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{Review.__name__}] ({self.id}) {self.__dict__}"