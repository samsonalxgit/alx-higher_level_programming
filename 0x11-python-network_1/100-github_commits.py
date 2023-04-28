#!/usr/bin/python3
'''List 10 commits starting with most recent of repo
rails by user rails
'''
import requests
import sys


if __name__ == '__main__':
    owner = sys.argv[2]
    repository = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner,
                                                              repository)
    request = requests.get(url)
    json_response = request.json()
    for i in json_response[:10]:
        print('{}: {}'.format(i.get('sha'),
                              i.get('commit').get('author').get('name')))
