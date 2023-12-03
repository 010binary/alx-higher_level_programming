#!/usr/bin/python3

def no_c(my_string):
    strings = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            strings += i
    return strings
