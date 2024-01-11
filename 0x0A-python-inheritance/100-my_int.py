#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and != using magic methods"""

    def __eq__(self, value):
        """Override == opeartor with != behavior with the __eq__ method"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior witht the __ne__ method"""
        return self.real == value
