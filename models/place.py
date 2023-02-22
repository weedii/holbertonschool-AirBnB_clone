#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{Place.__name__}] ({self.id}) {self.__dict__}"