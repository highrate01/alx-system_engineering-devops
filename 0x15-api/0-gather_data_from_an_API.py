#!/usr/bin/python3
"""
script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
from requests import get
import sys

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i.get('id') == int(sys.argv[1]):
            employee = i.get('name')

    for i in data:
        if i.get('userId') == int(sys.argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))
