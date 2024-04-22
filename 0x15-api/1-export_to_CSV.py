#!/usr/bin/python3
"""Export api to csv"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_of_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_of_user)

    user_name = res.json().get('username')
    task = url_of_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(USER_ID), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                USER_ID, user_name, completed, title_task))
