import requests
import json
import webbrowser
import credentials


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format", response.text)
    else:
        return content


def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get("https://api.thecatapi.com/v1/favourites", params, headers=credentials.headers)

    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search", headers=credentials.headers)

    return get_json_content_from_response(r)


def add_favourite_cat(catId, userId):

    catData = {
        "image_id": catId,
        "sub_id": userId
    }
    r = requests.post("https://api.thecatapi.com/v1/favourites", json=catData, headers=credentials.headers)

    return get_json_content_from_response(r)


userId = "agh2m"
name = "Arkadiusz"

favouriteCats = get_favourite_cats(userId)
print("Twoje ulubiona koty to: ", favouriteCats)


randomCat = get_random_cat()
print("Wylosowano kota: ", randomCat[0]["url"])

webbrowser.open_new_tab(randomCat[0]["url"])

addToFavorite = input("Czy chcesz dodoć do ulubionych? T/N ")

if (addToFavorite.upper() == "T"):
    print(add_favourite_cat(randomCat[0]["id"], userId))
else:
    print("No ok")
