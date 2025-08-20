# -*- coding : utf-8
# @Time: 2025-04-27
from flask import Flask, render_template, Blueprint
from flask_cors import CORS

app = Flask(__name__)

# 全局解决跨域问题
CORS(app, supports_credentials=True)

hello_route = Blueprint("hello", __name__, url_prefix="/hello")


# @app.route("/hello")
@hello_route.route("")
def hello():
    return "hello world"


@app.route("/cors")
def cors():
    return render_template("cors.html")


if __name__ == '__main__':
    app.register_blueprint(hello_route)
    app.run(port=5055, debug=True)
