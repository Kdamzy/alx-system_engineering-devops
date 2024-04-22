#!/usr/bin/python3
"""Export api to csv"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)
    USER_ID = sys.argv[1]
    url_of_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    user_res = requests.get(url_of_user)
    USERNAME = user_res.json().get('username')

    url_of_task = url_of_user + '/todos'
    task_res = requests.get(url_of_task)
    tasks = task_res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
