#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    A function that returns True
    if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class (type): The class to match the type of obj with.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
