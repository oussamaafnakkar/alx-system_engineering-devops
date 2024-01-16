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
        return data.get('data').get('subscribers')
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0
