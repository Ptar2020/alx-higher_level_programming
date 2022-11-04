#!/usr/bin/python3
"""This is the base class"""

class Base:
    """This is the base class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id != None:
            self.id = id
        Base.__nb_objects += 1 
        self.id = Base.__nb_objects
        

