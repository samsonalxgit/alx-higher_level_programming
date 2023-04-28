#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the X-Request-Id
"""

import urllib.request
from sys import argv

if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        headers = dict(response.info())
        if 'X-Request-Id' in headers:
            print(headers['X-Request-Id'])
