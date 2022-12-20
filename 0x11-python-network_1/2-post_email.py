#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.request(url, data)
    with urllib.request.urlopen(req) as response:
        message = response.read()
        print("{}".format(message.decode('utf-8')))
