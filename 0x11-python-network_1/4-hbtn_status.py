#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def fetch_status():
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_status()
