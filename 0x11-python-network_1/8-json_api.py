#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to a URL with that letter
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        letter = argv[1]
        r = requests.post(url, data={'q': letter})

    if len(argv) == 1:
        r = requests.post(url, data={'q': ""})

    try:
        json_dict = r.json()
        if json_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_dict['id'], json_dict['name']))

    except ValueError:
        print("Not a valid JSON")
