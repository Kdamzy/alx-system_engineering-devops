#!/usr/bin/python3
"""get data from an API and convert it to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_of_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_of_user)

    user_name = res.json().get('username')
    url_of_task = url_of_user + '/todos'
    res = requests.get(url_of_task)
    tasks = res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": user_name})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
