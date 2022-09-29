import random
"""
chestType = {'rare': 75, 'very rare': 20, 'epic': 4, 'legendary': 1}
dropFromChest = { 'rare': 1000, 'very rare': 4000, 'epic': 9000, 'legendary': 16000}
drawChestTotal = {'rare': 0, 'very rare': 0, 'epic': 0, 'legendary': 0}

moves = 5
chanceOfChest = 60
howMuchChestDropped = 0

def chest_spawn(chanceOfChest):
    chestdrawchance = random.uniform(0, 100)
    if (chanceOfChest <= chestdrawchance):
        return 1

    else:
        return 0

for x in range(moves):
    if (chest_spawn(chanceOfChest) == 1):
        drawChest = random.choices(list(chestType.keys()), list(chestType.values()))
        addNewChest = drawChestTotal.get(drawChest[0])
        drawChestTotal[drawChest[0]] = addNewChest + 1


goldInDrawnChests = {
    key: drawChestTotal[key] * dropFromChest[key]
    for key in drawChestTotal
}

print("draw cheast:", drawChestTotal)
print("Gold in each chest:", goldInDrawnChests)
print("Your gold:", sum(goldInDrawnChests.values()))


gameLenght = 5
goldSumary = 0

while (gameLenght > 0):

    gameAnswer = (input("Do you want to move forward?: "))
    chestSpawn = 60
    chestType = ['rare', 'very rare', 'epic', 'legendary']

    if (gameAnswer == "yes" ):
        chanceOfChestSpawn = random.uniform(0, 100)

        if (chestSpawn < chanceOfChestSpawn):
            chestYouDrop = random.choices(chestType, [75,20,4,1])
            if chestYouDrop == ['rare']:
                goldSumary += 1000
            elif chestYouDrop == ['very rare']:
                goldSumary += 4000
            elif chestYouDrop == ['epic']:
                goldSumary += 9000
            elif chestYouDrop == ['legendary']:
                goldSumary += 16000
            print("You find",chestYouDrop, "chest",)
            gameLenght -= 1

        elif (chestSpawn > chanceOfChestSpawn):
            print("There isn't an chest!")
            gameLenght -= 1
    else:
        print("You can only answer 'yes'")
        continue

    print("Your gold:", goldSumary)
"""
from enum import Enum


def findApproximateValue(value):
    lowestValue = value - 0.1 * value
    highestValue = value + 0.3 * value
    return random.randint(lowestValue, highestValue)


gameLength = 5
goldSumary = 0

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

ChestType = Enum('ChestType', {
    'Rare': 'Rzadka',
    'Epic': 'Epicka',
    'Mystical': 'Mistyczna',
    'legendary': 'legendarna'
}
)

chestTypeDictionary = {
    ChestType.Rare: 0.75,
    ChestType.Epic: 0.2,
    ChestType.Mystical: 0.04,
    ChestType.legendary: 0.01
}

chestTypeList = tuple(chestTypeDictionary.keys())
chestTypeProbability = tuple(chestTypeDictionary.values())

rewardForChests = {
    chestTypeList[reward]: (reward + 1) * (reward + 1) * 1000
    for reward in range(len(chestTypeList))
}

print("Welcome in game!")
print("You have 5 steps to make, Lets find out how much gold u can collect.")

while (gameLength > 0):

    gameAnswer = input("Do you want to move forward?: ")

    if (gameAnswer == "yes"):
        drawnEvent = random.choices(eventList, eventProbability)[0]

        if (drawnEvent == Event.Chest):
            print("You've drawn a Chest")
            drawnChest = random.choices(chestTypeList, chestTypeProbability)[0]
            print("You drawn", drawnChest.value, "chest")
            gamerReward = findApproximateValue(rewardForChests[drawnChest])
            goldSumary = goldSumary + gamerReward
            print(gamerReward)
            gameLength -= 1

        elif (drawnEvent == Event.Empty):
            print("You've drawn nothing!")
            gameLength -= 1

    else:
        print("You can only answer 'yes'")
        continue
print("You have acquired: ", goldSumary, "Gold")
