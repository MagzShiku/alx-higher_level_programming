#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the bod
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" == "200" ] && curl -s "$i"

