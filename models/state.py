#!/usr/bin/python3

"""
Class of State
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class that inherit from BaseModel Class"""

    name = ""

    # __str__ method
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{State.__name__}] ({self.id}) {self.__dict__}"
