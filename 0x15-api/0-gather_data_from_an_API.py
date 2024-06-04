#!/usr/bin/python3
"""
script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import re
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) > 1:

        if re.fullmatch(r'\d+', sys.argv[1]):

            employee_id = int(sys.argv[1])

            response = requests.get(f"{base_url}/users/{employee_id}")
            user = response.json()

            params = {"userId": employee_id}

            todos_response = requests.get(base_url + "/todos", params=params)

            todos = todos_response.json()

            completed = []

            for todo in todos:
                if todo.get("completed") is True:
                    completed.append(todo.get("title"))

            print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                len(completed), len(todos)))

            for complete in completed:
                print("\t{}".format(complete))
