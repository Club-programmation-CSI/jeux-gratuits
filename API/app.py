import steam
import epic
from flask import jsonify


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    steamGames = steam.fetchGames()
    epicGames = epic.fetchGames()
    return jsonify([*steamGames, *epicGames])
