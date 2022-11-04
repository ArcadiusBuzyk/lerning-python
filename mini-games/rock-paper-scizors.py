import random

player = 0
opponent = 0

possibleActions = ["paper", "rock", "scissors"]

while (player < 3) and (opponent < 3):

    playerAction = input("What u want to chose?: 'paper', 'rock', 'scissors'\n")
    opponentAction = random.choice(possibleActions)

    if (playerAction == "rock"):

        if (opponentAction == "paper"):
            opponent += 1
            print("opponent:", opponentAction)
            print("You lost !", "You:", player, "Computer:", opponent)
        elif (opponentAction == "scissors"):
            player += 1
            print("opponent:", opponentAction)
            print("You won point!", "You:", player, "Computer:", opponent)
        else:
            print("opponent:", opponentAction)
            print("draw")

    elif (playerAction == "paper"):

        if (opponentAction == "scissors"):
            opponent += 1
            print("opponent:", opponentAction)
            print("You lost !", "You:", player, "Computer:", opponent)
        elif (opponentAction == "rock"):
            player += 1
            print("opponent:", opponentAction)
            print("You won point!", "You:", player, "Computer:", opponent)
        else:
            print("opponent:", opponentAction)
            print("draw")

    elif (playerAction == "scissors"):

        if (opponentAction == "rock"):
            opponent += 1
            print("opponent:", opponentAction)
            print("You lost !", "You:", player, "Computer:", opponent)
        elif (opponentAction == "paper"):
            player += 1
            print("opponent:", opponentAction)
            print("You won point!", "You:", player, "Computer:", opponent)
        else:
            print("opponent:", opponentAction)
            print("draw")

if player == 3:
    print("You won game!")
elif opponent == 3:
    print("You lost game!")
