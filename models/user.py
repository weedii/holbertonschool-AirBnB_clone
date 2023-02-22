#!/usr/bin/python3

"""
Class of User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # __str__ method
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{User.__name__}] ({self.id}) {self.__dict__}"
