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
    headers = {"User-Agent": "Counter/3.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        if "data" in data:
            subscribers = data["data"].get("subscribers", 0)
            return subscribers

    except (requests.exceptions.RequestException, ValueError, KeyError):
        pass
        return 0
