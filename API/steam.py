import requests
from bs4 import BeautifulSoup


def fetchGames():
    response = requests.get(
        "https://store.steampowered.com/search/results?force_infinite=1&specials=1&maxprice=5"
        # "https://store.steampowered.com/search/results?force_infinite=1&maxprice=free&specials=1"
    )

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.select(".search_result_row")

    games = []

    for element in elements:
        title = element.select_one(".title").text
        appID = element.get("data-ds-appid")
        imageURL = (
            f"https://cdn.cloudflare.steamstatic.com/steam/apps/{appID}/header.jpg"
        )
        gameLink = element.get("href")

        game = {
            "name": title,
            "imageURL": imageURL,
            "gameLink": gameLink,
            "platform": "steam",
        }

        games.append(game)

    return games
