#!/usr/bin/python3
"""
script that accesses my github
"""

import requests
import sys

if __name__ == "__main__":
    """
    define my username and password
    """
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    data = response.json()

    print(data.get("id"))
