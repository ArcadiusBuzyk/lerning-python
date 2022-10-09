from matplotlib.backend_bases import key_press_handler
import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/todos/')


def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] is True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1
    return completedTaskFrequencyByUser


def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]


def user_with_top_completed_tasks(completedTaskFrequencyByUser):

    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    userIdWithMaxCompletedAmountOfTasks = []

    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            userIdWithMaxCompletedAmountOfTasks.append(userId)
    return userIdWithMaxCompletedAmountOfTasks


try:
    tasks = r.json()
except requests.exceptions.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    print(completedTaskFrequencyByUser)
    print(user_with_top_completed_tasks(completedTaskFrequencyByUser))
