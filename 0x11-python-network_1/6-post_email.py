#!/usr/bin/python3
"""
Display script that takes in a URL.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    request = requests.post(url, data=email)
    print(request.text)
