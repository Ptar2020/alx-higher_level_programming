#!/usr/bin/python3
import json
"""
This file contains a function
that creates an object from a "JSON FILE"
"""


def load_from_json_file(filename):
    """
    function that creates obj from json file
    """
    with open(filename) as file:
        new_obj = json.load(file)
    return (new_obj)
