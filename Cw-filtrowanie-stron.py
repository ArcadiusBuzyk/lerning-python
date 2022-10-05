import requests

fileName = str(input("Podaj nazwę pliku z adresami stron lub zamknij: "))

with (open(fileName, 'r', encoding='UTF-8')) as file:
    urlList = file.read().splitlines()
    for address in range(len(urlList)):
        url = urlList[address]
        response = requests.get(url)

        if (response.status_code == 200):
            try:
                with (open('działajaceStrony.txt', 'a+', encoding='UTF-8')) as file:
                    file.write(url + '\n')
                print(url, "strona działa poprawnie")
            except ConnectionError:
                continue
        else:
            with (open('nieDziałajaceStrony.txt', 'a+', encoding='UTF-8')) as file:
                file.write(url + '\n')
            print(url, "strona nie działa poprawnie")
