#!/usr/bin/python3
'''
Function to add 2 value (int or float) together
'''


def add_integer(a, b=98):
    '''
    func to add 2 vaues

    arg:
    a - int or float
    b - int or float

    Rasies:
    Type error if not [int , float]
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
