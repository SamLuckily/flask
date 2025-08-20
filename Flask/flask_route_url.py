# -*- coding : utf-8
# @Time: 2025-04-27
from flask import Flask, url_for, Blueprint, redirect

app = Flask(__name__)

login_route = Blueprint("login", __name__, url_prefix="/login")
index_route = Blueprint("index", __name__, url_prefix="/index")


@app.route("/helloworld")
def hello():
    return url_for("hello")


@login_route.route("")
def login():
    print("登录,成功后跳转到首页")
    # return url_for("index.index")
    # 跳转到首页路由，执行对应的视图函数
    return redirect(url_for("index.index"))


@index_route.route("")
def index():
    print("首页")
    return {"code": 0, "msg": "success"}


if __name__ == '__main__':
    app.register_blueprint(login_route)
    app.register_blueprint(index_route)
    app.run(port=5050, debug=True)
