#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit."""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'YourRedditUsername/1.0'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data.get('data', {}).get('children', [])

        if not children:
            print("No posts found.")
            return

        for index, child in enumerate(children[:10]):
            title = child.get('data', {}).get('title')
            print(f"{index + 1}. {title}")
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print(f"Error: {response.status_code}")

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
