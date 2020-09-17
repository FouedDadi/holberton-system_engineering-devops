#!/usr/bin/python3
"""
get the number of subscribers for a specific subreddit
"""

import requests


def top_ten(subreddit):
    """
    function to get subscribers
    """
    user = {'User-Agent': 'lycan619'}
    request = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit), headers=user).json()
    if request is None:
        print('None')
    else:
        dt = request.get('data')
        child = dt.get('children')
        if dt and child:
            for data in child(limit=10):
                title = data.get('data').get('title')
            print(title)
