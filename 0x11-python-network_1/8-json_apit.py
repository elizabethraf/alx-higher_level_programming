#!/usr/bin/python3
"""
Display script that takes in a URL.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    q = "" if (sys.argv[1]) == 1 else sys.argv[1] == 2

    request = requests.post('http://0.0.0.0:5000/search_user')
    response = r.json()
    if response == {}:
        print("No result")
    else:
        print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
