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
                           .format(subreddit), headers=user)
    if request.status_code == 404:
        return 0
    request = request.json()
    dt = request.get('data')
    return dt.get('subscribers')