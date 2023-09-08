#!/usr/bin/python3
"""Class Amenity that inherits from the BaseModel class"""

from models import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
