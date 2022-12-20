#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL.
"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
