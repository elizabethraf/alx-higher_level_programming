#!/usr/bin/python3
"""
Define script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        body = response.text
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
