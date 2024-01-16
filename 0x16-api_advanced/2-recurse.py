#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursive function to get titles of hot articles from a subreddit."""
    if not hot_list:
        hot_list = []  # Initialize hot_list if not provided

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'YourRedditUsername/1.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data.get('data', {}).get('children', [])

        if not children:
            return hot_list  # Base case: no more articles

        for child in children:
            title = child.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        after = data.get('data', {}).get('after')
        return recurse(subreddit, hot_list, after)  # Recursive call with updated 'after'
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
