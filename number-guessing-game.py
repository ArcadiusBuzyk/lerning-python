import random

while True:
    print("Chose difficulty: level 'easy' 'normal' 'hard'")

    difficultylevel = str(input("Difficulty lever: "))
    if difficultylevel == "easy":
        attemptLimit = 15
    elif difficultylevel == "normal":
        attemptLimit = 10
    elif difficultylevel == "hard":
        attemptLimit = 6

    secretNumber = random.randint(0,100)
    attemptNumber = 0

    print("You choose",  difficultylevel,  "level,",  "now i m gonna think about number between 0 and 100")

    while attemptNumber < attemptLimit:
        number = int(input("Guess number i m thinking about? :"))
        if number < secretNumber:
            print("My number is higher.")
        elif number > secretNumber:
            print("My number is lower.")
        elif number == secretNumber:
            print("Congratulations, i was thinking about: ", + number)
            break
        attemptNumber += 1
    if attemptNumber == attemptLimit:
        print("GAME OVER! You lose!")
