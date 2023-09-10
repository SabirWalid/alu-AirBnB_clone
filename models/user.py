#!/usr/bin/python3
"""Class representing a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Details of a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """def __init__(self, *args, **kwargs):
        Initialize a User instance
        super().__init__(*args, **kwargs)"""
