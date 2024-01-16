#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'YourRedditUsername/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers_count = data.get('data', {}).get('subscribers', 0)
        return subscribers_count
    elif response.status_code == 404:
        return 0  # Return 0 directly for invalid subreddit
    else:
        return 0  # Return 0 for any other errors
