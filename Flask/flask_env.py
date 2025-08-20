# -*- coding : utf-8
# @Time: 2025-04-15

from flask import Flask

# 创建Flask应用程序实例
app = Flask(__name__)


# 定义路由和视图函数
@app.route("/")
def hello():
    return "hello Flask"


if __name__ == '__main__':
    app.run()
