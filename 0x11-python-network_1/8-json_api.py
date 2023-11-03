#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    """
    define url
    """
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    try:
        response = requests.post(url, data={"q": letter})
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))

        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
