from curses import raw
import requests
from bs4 import BeautifulSoup


def fetchGames():
    response = requests.get(
        "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=fr&country=FR&allowCountries=FR"
    )

    json = response.json()

    rawGames = json["data"]["Catalog"]["searchStore"]["elements"]
    games = []
    for rawGame in rawGames:
        if "discount" not in rawGame["price"]["totalPrice"]:
            continue
        if (
            rawGame["price"]["totalPrice"]["discount"] == 0
            or rawGame["price"]["totalPrice"]["discountPrice"] != 0
        ):
            continue
        game = {
            "name": rawGame["title"],
            "imageURL": rawGame["keyImages"][0]["url"],
            "gameLink": "https://store.epicgames.com/fr/free-games",
            "platform": "epic games",
        }
        games.append(game)

    return games
