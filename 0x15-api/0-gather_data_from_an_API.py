#!/usr/bin/python3
"""
script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"

    employee_id = sys.argv[1]

    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)
    user = response.json()

    params = {"userid": employee_id}

    todos_response = requests.get(f"{base_url}/todos", params=params)

    todos = todos_response.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("employee {} is done with tasks({}/{})".format(user.get("name"),
          len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
