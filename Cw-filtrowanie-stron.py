import requests
while True:
    fileName = str(input("Podaj nazwę pliku z adresami stron lub zamknij: "))

    if (fileName == "zamknij"):
        break

    else:
        def filter_websides(path):

            with (open(path, 'r', encoding='UTF-8')) as file:
                urlList = file.read().splitlines()
                for address in range(len(urlList)):
                    url = urlList[address]
                    response = requests.get(url)
                    if (response.status_code == 200):
                        with (open('działajaceStrony.txt', 'a', encoding='UTF-8')) as file:
                            file.write(url + '\n')
                            print(url, "strona działa poprawnie")
                    elif (response.status_code == 404):
                        with (open('nieDziałajaceStrony.txt', 'a', encoding='UTF-8')) as file:
                            file.write(url + '\n')
                            print(url, "strona nie działa poprawnie")

        fileContent = filter_websides(fileName)
