#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL.
"""
from urllib.parse import urlencode
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urlencode(email).encode()

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        message = response.read()
        print("{}".format(message.decode('utf-8')))
