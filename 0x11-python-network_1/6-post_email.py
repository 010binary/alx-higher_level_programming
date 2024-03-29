#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
  - In this case it an email
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    message = {"email": sys.argv[2]}

    response = requests.post(url, data=message)
    print(response.text)
