import steam
import epic
from flask import jsonify
from flask_cors import CORS

from flask import Flask

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    games = []
    try:
        steamGames = steam.fetchGames()
        games.append(steamGames)
    except Exception as e:
        print(e)
    try:
        epicGames = epic.fetchGames()
        games.append(epicGames)
    except Exception as e:
        print(e)
        
    return jsonify([*steamGames, *epicGames])
