#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in
order to solve this challenge.
"""

import requests
import sys

if __name__ == "__main__":
    """
    define repo and owner
    """
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        vvv = commit.get("vvv")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{vvv}: {author_name}")
