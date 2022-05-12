import requests
from bs4 import BeautifulSoup


def fetchGames():
    response = requests.get(
        "https://store.steampowered.com/search/results?force_infinite=1&specials=1"
        # "https://store.steampowered.com/search/results?force_infinite=1&maxprice=free&specials=1"
    )

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.select(".search_result_row")

    games = []

    for element in elements:
        title = element.select_one(".title").text
        imageURL = element.select_one("img").get("src")
        gameLink = element.get("href")

        game = {
            "name": title,
            "imageURL": imageURL,
            "gameLink": gameLink,
            "platform": "steam",
        }

        games.append(game)

    return games
