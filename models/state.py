#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{State.__name__}] ({self.id}) {self.__dict__}"
