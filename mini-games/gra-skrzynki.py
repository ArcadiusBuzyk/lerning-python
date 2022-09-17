import random

chestType = {'rare': 75, 'very rare': 20, 'epic': 4, 'legendary': 1}
dropFromChest = { 'rare': 1000, 'very rare': 4000, 'epic': 9000, 'legendary': 16000}
drawChestTotal = {'rare': 0, 'very rare': 0, 'epic': 0, 'legendary': 0}

moves = 5
chanceOfChest = 60


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

