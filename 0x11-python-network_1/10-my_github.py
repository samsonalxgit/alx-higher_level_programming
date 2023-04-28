#!/usr/bin/python3
"""
Takes Github credentials and displays the id of the user using the Github API
"""

import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, password))
    if r.status_code != 200:
        print("None")
    else:
        json_dict = r.json()
        print(json_dict['id'])
