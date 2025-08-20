# -*- coding : utf-8
# @Time: 2025-04-23
from flask import Blueprint, Flask

app = Flask(__name__)

# 1、声明蓝图
goods_router = Blueprint(name="goods", import_name=__name__)
user_router = Blueprint("user", __name__, url_prefix="/user")


# 2、定义路由
@goods_router.route("/")
def index():
    return {"code": 0, "msg": "success", "data": []}


@goods_router.route("/add", methods=["POST"])
def add_goods():
    return {"code": 0, "msg": "add success", "datas": ["goods1"]}


@user_router.route("")
def user_list():
    return {"code": 0, "msg": "add success", "datas": []}


@user_router.route("/login", methods=["POST"])
def login():
    return {"code": 0, "msg": "login success"}


if __name__ == '__main__':
    # 注册蓝图
    app.register_blueprint(goods_router)
    app.register_blueprint(user_router)
    # 启动应用
    app.run(port=5055, debug=True)
