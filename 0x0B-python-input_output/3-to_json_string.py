#!/usr/bin/python3
""" defines a function that changes strings to json"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
