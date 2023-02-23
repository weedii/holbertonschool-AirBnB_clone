#!/usr/bin/python3

"""
Class of City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class that inherit from BaseModel Class"""

    state_id = ""
    name = ""

    # __str__ method
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{City.__name__}] ({self.id}) {self.__dict__}"
