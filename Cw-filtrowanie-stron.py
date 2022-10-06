import requests


def filter_web(path):

    with (open(path, 'r', encoding='UTF-8')) as file:
        urlList = file.read().splitlines()
        for address in range(len(urlList)):
            try:
                url = urlList[address]
                response = requests.get(url)
                if (response.status_code == 200):
                    with (open('działajaceStrony.txt', 'a', encoding='UTF-8')) as file:
                        file.write(url + "\n")
            except requests.exceptions.ConnectionError:
                with (open('nieDziałajaceStrony.txt', 'a', encoding='UTF-8')) as file:
                    file.write(url + "\n")


fileName = str(input("Podaj nazwę pliku: "))

filter_web(fileName)
