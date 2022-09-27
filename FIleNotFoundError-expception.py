while True:
    
    fileName = input("Podaj nazwę pliku lub zamknij: ")
    if (fileName == "zamknij"):
        break

    else:
        def file_Opener(path):
            try:
                with open(path, "r", encoding="UTF-8")as file:
                        return  print(file.read())

            except FileNotFoundError:
                print("Nie znaleziono pliku o takiej nazwie, podaj prawidłową nazwę pliku")
                return

        fileContent = file_Opener(fileName)

