#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


def fetch_url():
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__nain__":
    fetch_url()
