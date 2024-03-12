#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


def search_user():
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
