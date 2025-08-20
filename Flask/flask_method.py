# -*- coding : utf-8
# @Time: 2025-04-17


from flask import Flask

# 创建Flask应用程序实例
app = Flask(__name__)


# get请求
@app.route("/get")
def get():
    return "Method is GET"


@app.route("/get_method", methods=["GET"])
def get_method():
    return "GET method success."


@app.route("/post", methods=["POST"])
def post():
    return "Method is POST"


@app.route("/delete", methods=["DELETE"])
def delete():
    return "Method is DELETE"


@app.route("/put", methods=["PUT"])
def put():
    return "Method is PUT"


@app.route("/more", methods=["GET", "post"])
def more():
    return "Method is GET or POST"


if __name__ == '__main__':
    app.run()
