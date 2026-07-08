#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get("{}/todos?userId={}".format(base, user_id)).json()

    done = [t for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for t in done:
        print("\t {}".format(t.get("title")))
