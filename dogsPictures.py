import requests
import json
import webbrowser


params = {
    
}

r = requests.get("https://dog.ceo/api/breeds/list/all", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    dogBreeds = content["message"]
    for dog in dogBreeds:
        choice = input