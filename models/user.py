#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{User.__name__}] ({self.id}) {self.__dict__}"
