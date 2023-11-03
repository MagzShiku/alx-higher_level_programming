#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """
    define email and url
    """

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()

    print(body.decode("utf-8"))
