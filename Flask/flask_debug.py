# -*- coding : utf-8
# @Time: 2025-04-23

from flask import Flask

# 创建Flask应用程序
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Flask!"


@app.route("/dict")
def dict_res():
    return {"status": 0}


# 运行应用程序
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5055, debug=True)
