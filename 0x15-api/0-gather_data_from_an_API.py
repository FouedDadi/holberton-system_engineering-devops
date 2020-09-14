#!/usr/bin/python3
"""
[summary]
"""

import requests
from sys import argv

if __name__ == '__main__':
    lst = []
    id = argv[1]
    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(id)).json()
    quest = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': id}).json()
    name = resp.get('name')
    for to in quest:
        if to.get('completed') is True:
            lst.append(to)
    print("Employee {} is done with tasks({}/{}):".format(name, len(lst),
                                                          len(quest)))
    for title in lst:
        print("\t {}".format(title.get('title')))
