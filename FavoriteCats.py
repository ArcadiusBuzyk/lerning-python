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

    return get_json_content_from_response(r)[0]


def add_favourite_cat(catId, userId):

    catData = {
        "image_id": catId,
        "sub_id": userId
    }
    r = requests.post("https://api.thecatapi.com/v1/favourites", json=catData, headers=credentials.headers)

    return get_json_content_from_response(r)


def remove_favourite_cat(favouriteCatId):
    r = requests.delete("https://api.thecatapi.com/v1/favourites/" + favouriteCatId, headers=credentials.headers)

    return get_json_content_from_response(r)


userId = "agh2m"
name = "Arkadiusz"

favouriteCats = get_favourite_cats(userId)


while True:

    randomCat = get_random_cat()
    print("Wylosowano kota: ", randomCat["url"])
    webbrowser.open_new_tab(randomCat["url"])
    addToFavorite = input("Czy chcesz dodać do ulubionych? T/N ")

    if (addToFavorite.upper() == "T"):

        resultFromAddingFavouriteCat = add_favourite_cat(randomCat["id"], userId)
        newlyAddedCatInfo = {resultFromAddingFavouriteCat["id"]: randomCat["url"]}

        favouriteCatsById = {
            favouriteCat["id"]: favouriteCat["image"]["url"]
            for favouriteCat in favouriteCats
        }
        favouriteCatsById.update(newlyAddedCatInfo)

    else:
        print("No ok")
        break


print("Twoje ulubiona koty to: ", favouriteCatsById("id")("url"))
favouriteCatId = input("Czy chcesz usunąć kota? ")
print(remove_favourite_cat(favouriteCatId))
