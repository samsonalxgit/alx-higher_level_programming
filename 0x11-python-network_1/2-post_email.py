#!/usr/bin/python3
"""
    a Python script that takes in a URL and an
    email, sends a POST request to the passed URL
    with the email as a parameter, and displays the
    body of the response (decoded in utf-8)
"""

from urllib import request, parse
from sys import argv

if __name__ == '__main__':

    try:
        url = argv[1]
        email = argv[2]

        data = parse.urlencode({
            "email": email
        })
        data = data.encode('ascii')

        with request.urlopen(url, data) as response:
            print(response.read().decode('utf-8'))
    except:
        pass
