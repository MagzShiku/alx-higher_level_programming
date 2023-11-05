#!/bin/bash
# takes in a URL, sends a GET request to the URL, and display body
curl -s -o /dev/null -w "%{http_code}" $1 | xargs -I % sh -c '[ "%" == "200" ] && curl -s $1'
