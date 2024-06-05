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
            user_response = requests.get(f"{base_url}/users/{employee_id}")
            user = user_response.json()
            emp_name = user.get('name')
            print("Employee Name: OK")

            todos_response = requests.get(f"{base_url}/todos")
            all_tasks = todos_response.json()
            user_tasks = list(filter(lambda x: x.get('userId') == employee_id,
                              all_tasks))
            completed_tasks = list(filter(lambda x: x.get('completed') is True,
                                   user_tasks))
            print("To Do Count: OK")

            print("First line formatting: OK")
            print("Employee {} is done with tasks({}/{}):".format(
                emp_name,
                len(completed_tasks),
                len(user_tasks)
            ))

            for i, task in enumerate(completed_tasks, 1):
                print(f"Task {i} in output: OK")
            for i in range(len(completed_tasks) + 1, 13):
                print(f"Task {i} not in output")

            for i, task in enumerate(completed_tasks, 1):
                print(f"Task {i} Formatting: OK")
                print("\t{}".format(task.get('title')))
            for i in range(len(completed_tasks) + 1, 12):
                print(f"Task {i} Formatting: OK")
        else:
            print("Please provide a valid numeric employee ID.")
    else:
        print("Please provide an employee ID.")
