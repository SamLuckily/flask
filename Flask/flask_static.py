# -*- coding : utf-8
# @Time: 2025-04-26
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def show_icon():
    return render_template("static.html")


if __name__ == '__main__':
    app.run(port=5050, debug=True)
