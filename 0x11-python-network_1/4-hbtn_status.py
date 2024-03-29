#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
this can be moded if need be 
"""
import requests

url = "https://intranet.hbtn.io/status"

if __name__ == '__main__':
    response = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
