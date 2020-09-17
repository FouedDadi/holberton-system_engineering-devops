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
    if request is None:
        print('None')
        return
    child = request.get('data').get('children')
    if child:
        for data in child[:10]:
            title = data.get('data').get('title')
            print(title)
