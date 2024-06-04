#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import re
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) < 2:
        print("Please provide an employee ID.")
        sys.exit(1)

    user_id = sys.argv[1]
    if not re.fullmatch(r'\d+', user_id):
        print("Please provide a valid numeric employee ID.")
        sys.exit(1)

    try:
        response = requests.get(f"{base_url}/users/{user_id}")
        response.raise_for_status()  # Raise an exception for bad status codes
        user = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        sys.exit(1)

    username = user.get("username")
    params = {"userId": user_id}

    try:
        todos_response = requests.get(f"{base_url}/todos", params=params)
        todos_response.raise_for_status()
        todos = todos_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching todos: {e}")
        sys.exit(1)

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_id,
                username,
                str(todo.get("completed")).lower(),
                todo.get("title")
            ])

    print(f"Data exported to {user_id}.csv")
