#!/usr/bin/python3
"""Class State that inherits from the BaseModel class"""

from models import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
