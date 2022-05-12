import requests
from bs4 import BeautifulSoup


def fetchGames():
    response = requests.get(
        "https://store.epicgames.com/graphql?operationName=getCatalogOffer&variables={%22locale%22:%22fr%22,%22country%22:%22FR%22,%22offerId%22:%22b97151524f9a4815961e9a17ec3c990e%22,%22sandboxId%22:%2225d726130e6c4fe68f88e71933bda955%22}&extensions={%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%22ff096572d1065b7058e64c86ce4630bfb5727955056fe910b3f29cb50568fdd7%22}}"
    )

    json = response.json()

    rawGame = json["data"]["Catalog"]["catalogOffer"]
    game = {
        "name": rawGame["title"],
        "imageURL": rawGame["keyImages"][0]["url"],
        "gameLink": "https://store.epicgames.com/fr/free-games",
        "platform": "epic games",
    }

    games = []
    games.append(game)
    return games
