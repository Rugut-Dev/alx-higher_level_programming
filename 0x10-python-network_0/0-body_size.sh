#!/bin/bash
# send request to a URL with curl
curl -s "$1" | wc -c
