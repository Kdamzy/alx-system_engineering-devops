#!/usr/bin/python3
"""Recursive function that queries the Reddit api"""
from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles of all hot articles for a given
    subreddit.
    """
    if after is None:
        return hot_list

    url = REDDIT + "r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    r = get(url, headers=HEADERS, params=params, allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        js = r.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

    except Exception:
        return None

    return recurse(subreddit, hot_list, after)
