#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


def send_post_request():
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    reqest = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(reqest) as response:
        res_body = response.read().decode('utf-8')
        print(res_body)


if __name__ == "__main__":
    send_post_request()
