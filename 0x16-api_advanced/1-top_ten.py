#!/usr/bin/python3
"""prints the titles of the first 10 hot post"""

from requests import get


def top_ten(subreddit):
    """function that prints the titles of first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "YourUserAgent"
        }
    response = get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("No posts found.")
    else:
        print(None)
