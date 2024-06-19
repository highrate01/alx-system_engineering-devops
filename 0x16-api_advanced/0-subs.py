#!/usr/bin/python3
"""
Defines a script that queries the number of subscribers for a
given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for
    given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']

        return subscribers
    else:
        return 0
