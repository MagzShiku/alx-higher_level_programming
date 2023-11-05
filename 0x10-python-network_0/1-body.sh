#!/bin/bash
# takes in a URL, sends a GET request to the URL, and display body
curl -s $1 | awk '/HTTP\/1.1 200 OK/ { flag=1; next } flag { print }'
