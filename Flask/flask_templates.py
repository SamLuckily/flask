# -*- coding : utf-8
# @Time: 2025-04-26
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("cybercharge.html")


@app.route("/data")
def cc():
    return render_template("cybercharge.html", name="宝箱夺金")


@app.route("/games")
def games():
    games_info = {
        "name": "宝箱夺金",
        "bet": "GEM"
    }
    return render_template("cybercharge.html", games=games_info)


@app.route("/game")
def game():
    game_info = [
        {
            "name": "宝箱夺金",
            "bet": "GEM"
        },
        {
            "name": "飞刀",
            "bet": "RMB"
        }
    ]
    return render_template("game.html", game=game_info)


@app.route("/extend")
def extend():
    return render_template("son.html")


if __name__ == '__main__':
    app.run(port=5055, debug=True)
