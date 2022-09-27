"""
with open("imionaNazwiska.txt", "w", encoding="UTF-8") as file:
    file.write("Arkadiusz Buz\nMeadow\nCarla Baker\nLily-May Rosas\nInez Emerson\nStuart Harrington\nLemar Calderon\nZahraa Joyner\nNiam Martin\nEzmae Hull\nAthena Frost\nArkadiusz marx")
"""    
        

namesAndSurnames = []

with open("imionaNazwiska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesAndSurnames.append(tuple(line.replace("\n", "").split(" ")))
print(namesAndSurnames)

with open("imiona.txt", "w", encoding="UTF-8") as file:
    for item in namesAndSurnames:
        file.write(item [0] + "\n")

with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for item in namesAndSurnames:
        try:
            file.write(item [1] + "\n")
        except IndexError:
            file.write("\n")
