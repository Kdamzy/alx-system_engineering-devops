#!/usr/bin/python3
"""querier the Reddit API"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the
    number of subscribers(not active users, total subscribers)
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "YourUserAgent"
        }
    response = get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return(0)
