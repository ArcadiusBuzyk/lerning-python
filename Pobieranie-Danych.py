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


def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):

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
    userWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print(userWithTopCompletedTasks)

"""
# sposob 1
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()


def give_cookie_to_top_users(userWithTopCompletedTasks):
    userNameWithCookie = []
    for user in users:
        if (user["id"] in userWithTopCompletedTasks):
            userNameWithCookie.append(user["name"])
    return userNameWithCookie


usersWithCookie = give_cookie_to_top_users(userWithTopCompletedTasks)
print("Wreczam ciasteczko osobom o imieniu :", usersWithCookie)

# sposob 2
for userId in userWithTopCompletedTasks:
    r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    user = r.json()
    print("Wreczam ciasteczko osobie o imieniu: ", user["name"])
"""

# sposob 3


def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="

    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&id="

    return conj_param


conj_param = change_list_into_conj_of_param(userWithTopCompletedTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj_param)

users = r.json()
for user in users:
    print("Wreczam ciasteczko osobie o imieniu: ", user["name"])
