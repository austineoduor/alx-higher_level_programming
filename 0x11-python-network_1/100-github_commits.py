#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve the given challenge
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com'
    uri = '{0}/repos/{1}/{2}/commits'.format(url, argv[2], argv[1])
    r = requests.get(uri)
    commits = r.json()

    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
