# -*- coding : utf-8
# @Time: 2025-04-23
from flask import Flask, jsonify, render_template, make_response

# 创建一个flask应用程序实例

app = Flask(__name__)


# 定义返回文本类型的响应接口
@app.route("/text")
def text_res():
    return "文本类型响应"


# 定义返回元组格式的响应接口
@app.route("/tuple")
def tuple_res():
    return "你好", 200, {"name": "Sam"}


# 返回JSON格式响应体
@app.route("/json")
def json_res():
    # return jsonify({"status": 0})
    return jsonify(status=0, name="lily", age=28)


# 直接返回字典 JSON格式响应
@app.route("/dict")
def dict_res():
    return {"status": 0}


# 返回html
@app.route("/html")
def html_res():
    # 调用render_template()方法， 传入html文件名
    # demo.html 文件必须放在py 文件同级的 templates 目录下
    return render_template("demo.html")


# 返回更复杂的响应数据
@app.route("/")
def index():
    # 获取响应对象
    res = make_response(render_template("demo.html"))
    # 设置cookie
    res.set_cookie("username", 'lily')
    # 设置响应头信息
    res.headers["name"] = "Sam"
    return res


# 运行应用程序
if __name__ == '__main__':
    app.run()
