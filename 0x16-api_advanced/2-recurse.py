#!/usr/bin/python3
"""Defines a recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The subreddit to search for hot posts.
        hot_list (list, optional): A list to store the hot post titles.
            Defaults to an empty list.
        after (str, optional): The "after" parameter for the Reddit API.
            Defaults to an empty string.
        count (int, optional): The count of posts retrieved so far.
            Defaults to 0.

    Returns:
        list: A list of hot post titles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
                v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for submission in results.get("children"):
        hot_list.append(submission.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
