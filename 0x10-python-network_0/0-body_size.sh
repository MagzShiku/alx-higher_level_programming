#!/bin/bash
#  takes in a URL, sends a request to that URL, and displays the size

[ $# -eq 0 ] && echo "URL is required." && exit 1
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
