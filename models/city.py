#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{City.__name__}] ({self.id}) {self.__dict__}"
