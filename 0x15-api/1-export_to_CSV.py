#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    user_id = sys.argv[1]

    response = requests.get(base_url + "/users/{}".format(user_id))

    user = response.json()
    username = user.get("username")

    params = {"userId": user_id}

    todos_response = requests.get(base_url + "/todos", params=params)

    todos = todos_response.json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                            todo.get("title")])
