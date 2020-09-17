#!/usr/bin/python3
"""
get the number of subscribers for a specific subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    function to get subscribers
    """
    user = {'User-Agent': 'lycan619'}
    request = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit), headers=user).json()
    if request is None:
        return 0
    else:
        dt = request.get('data')
        if dt:
            return dt.get('subscribers')
