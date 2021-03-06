#!/usr/bin/python3
"""
python script that saves data to csv file
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    lst = []
    id = argv[1]
    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(id)).json()
    quest = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': id}).json()
    name = resp.get('username')
    with open('{}.csv'.format(id), "w") as csv_file:
        writing = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for to in quest:
            Title = to.get('title')
            completion = to.get('completed')
            writing.writerow([id, name, completion, Title])
