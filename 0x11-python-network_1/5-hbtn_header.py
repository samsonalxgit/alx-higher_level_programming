#!/usr/bin/python3
"""
Sends a request to URL and displays the X-Request-Id variable using requests
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    r = requests.get(url)
    if 'X-Request-Id' in r.headers:
        print(r.headers['X-Request-Id'])
