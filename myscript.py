from user import User

users = [User() for _ in range(8)]

for user in users:
    print(user.id)
