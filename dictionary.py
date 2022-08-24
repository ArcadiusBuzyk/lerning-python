listOfWords = {}

while True :
    print("Main menu: '1'-add word, '2'-search word, '3'-delete word, '4'-close ")
    command = int(input("What do you want to do?: "))

    if command == 1 :
        key = str(input("Enter word: "))
        definition = str(input("Enter definition of the word: "))

        listOfWords.update({key: definition}) 
        print("Word added successfuly ")

    elif command == 2 :
        key = str(input("What word to serch?: "))
        print(listOfWords[key])
    
    elif command == 3 :
        key = str(input("What word you want to delete?: "))
        del(listOfWords[key])
        print("Word deleted successful")

    elif command == 4 :
        print("You chose option: 'close'")
        break
    else:
        print("Wrong command! Try again.")

    
    
