#!/bin/bash
# send request to URL
curl -s -o /dev/null -w "%{http_code}" "$1"
