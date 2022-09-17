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
"""
gameLenght = 5
goldSumary = 0


while (gameLenght > 0):

    gameAnswer = int(input("Do you want to move forward? 1 - yes 2 - no : "))
    chestSpawn = 60
    chestType = ['rare', 'very rare', 'epic', 'legendary']
    
    if (gameAnswer == 1 ):
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
               
    print("Your gold:", goldSumary)   