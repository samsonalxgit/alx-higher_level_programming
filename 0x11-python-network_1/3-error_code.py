#!/usr/bin/python3
"""
Sends a request to the URL and manages HTTP error exceptions"
"""

import urllib.request
import urllib.error
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            utf = html.decode('utf-8')
        print(utf)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
