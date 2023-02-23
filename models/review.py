#!/usr/bin/python3

"""
Class of Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class that inherit from BaseModel Class"""

    place_id = ""
    user_id = ""
    text = ""

    # __str__ method
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{Review.__name__}] ({self.id}) {self.__dict__}"
