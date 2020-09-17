#!/usr/bin/python3
"""
get the hot titles for a specific subreddit
"""

import requests


def top_ten(subreddit):
    """
    function to get hot titles
    """
    user = {'User-Agent': 'lycan619'}
    request = requests.get('https://www.reddit.com/r/{}/hot.json'
                           .format(subreddit), headers=user).json()
    if request.get('error') == 404:
        print('None')
    child = request.get('data').get('children')
    for data in child[:10]:
        title = data.get('data').get('title')
        print(title)
