import random

player = 0
opponent = 0

a = ['paper', 'rock', 'scisors']

"paper" > "rock"
"rock" > "scisors"
"scisors" > "paper"

while (player < 3) and (opponent < 3):

    playerChoice = input("What u want to chose?: 'paper', 'rock', 'scisors'\n")
    opponentChoice  = random.choice(a)

    if (playerChoice == opponentChoice):
        print("opponent:", opponentChoice )
        print("draw")

    elif (playerChoice < opponentChoice):
        print("opponent:", opponentChoice )
        player += 1
        print("You won point!", "You:", player, "Computer:", opponent )
        
    elif (opponentChoice < playerChoice):
        print("opponent:", opponentChoice )
        opponent += 1
        print("You lost !", "You:", player, "Computer:", opponent )

if player == 3:
    print("You won game!")
elif opponent == 3:
    print("You lost game!")

       


