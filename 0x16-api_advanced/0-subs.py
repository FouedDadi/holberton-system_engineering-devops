#!/usr/bin/python3
"""
[summary]
"""

import requests


def number_of_subscribers(subreddit):
    """[summary]
    """
    user = {'User-Agent': 'lycan619'}
    request = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit), headers=user).json()
    if request:
        dt = request.get('data')
        if dt:
            return dt.get('subscribers')
    return 0
