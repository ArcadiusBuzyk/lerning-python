import random

print("Chose difficulty level 'easy' 'normal' 'hard'")
difficultylevel = int(input("Difficulty lever: "))

easy = 15
normal = 10
hard = 6

secretNumber = random.randint(0,100)
attemptNumber = 0

if attemptNumber < difficultylevel:
    number = int(input("What is number i m thinking about? :"))
    if number < secretNumber:
        print("My number is higher.")
    elif number > secretNumber:
        print("MY number is lower.")
    elif number == secretNumber:
        print("Congratulations, i was thinking about: " + secretNumber)
    attemptNumber += 1
