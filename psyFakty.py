import requests
import json

while True:

    print("This is a random dogs facts program!")
    answer = int(input("What u want to do? 1 - Get to know a dogs facts. 2 - Leave. : "))

    if (answer == 1):

        params = {
            "number": int(input("How many facts u want?: "))
        }
        r = requests.get("http://dog-api.kinduff.com/api/facts", params)

        try:
            content = r.json()
        except json.decoder.JSONDecodeError:
            print("Niepoprawny format")
        else:
            dogFact = content["facts"]
            x = 0
            for dog in dogFact:
                x += 1
                print(x, "-", dog)

    elif (answer == 2):
        break
