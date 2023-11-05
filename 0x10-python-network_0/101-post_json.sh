#!/bin/bash
# cript that sends a JSON POST request to a URL passed as the first argument, and displays the body
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
