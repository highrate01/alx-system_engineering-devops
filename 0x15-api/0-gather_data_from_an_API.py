#!/usr/bin/python3
"""
script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import re
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            user_response = requests.get(f"{base_url}/users/{employee_id}")
            user = user_response.json()
            emp_name = user.get('name')

            todos_response = requests.get(f"{base_url}/todos")
            all_tasks = todos_response.json()
            user_tasks = list(filter(lambda x: x.get('userId') == employee_id,
                              all_tasks))
            completed_tasks = list(filter(lambda x: x.get('completed'),
                                          user_tasks))

            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(user_tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t{}'.format(task.get('title')))
