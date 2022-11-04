import random

while True:
    print("Chose difficulty: level 'easy' 'normal' 'hard'")

    difficultyLevel = str(input("Difficulty lever: "))
    if difficultyLevel == "easy":
        attemptLimit = 15
    elif difficultyLevel == "normal":
        attemptLimit = 10
    elif difficultyLevel == "hard":
        attemptLimit = 6

    secretNumber = random.randint(0, 100)
    attemptNumber = 0

    print("You choose", difficultyLevel, "level,", "now i m gonna think about number between 0 and 100")

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
