#!/bin/bash
# takes in a URL, sends a GET request to the URL, and display body
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
