#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL
displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    """
    define url
    """
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get("X-Request-Id")

    print(request_id)
