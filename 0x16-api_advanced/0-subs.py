#!/usr/bin/env python3
"""
0-subs.py - Fetches the number of subscribers
for a given subreddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    # Construct the URL for the subreddit information endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid API restrictions
    headers = {"User-Agent": "custom_user_agent"}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to extract subscriber count
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        else:
            # Return 0 for invalid subreddits or other errors
            return 0
    except Exception as e:
        # Print an error message if an exception occurs during the request
        print(f"Error: {e}")
        return 0
