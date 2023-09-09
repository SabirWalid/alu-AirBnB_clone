#!/usr/bin/python3
"""Class city that inherits from the BaseModel class"""

from models import BaseModel


class City(BaseModel):
    """City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
