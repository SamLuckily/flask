# -*- coding : utf-8
# @Time: 2025-04-22

from flask import Flask, request
from werkzeug.utils import secure_filename

# 创建flask应用程序实例


app = Flask(__name__)


# 定义获取请求参数的接口
@app.route("/user")
def get_user():
    # 获取客户端请求中URL拼接的请求参数
    url_param = request.args
    # 查看获取到请求参数的类型
    print(type(url_param))
    # 获取请求参数中，username对应的值
    username = url_param.get("username")
    return f"Hello{username}"


@app.route("/data", methods=["POST"])
def json_data():
    # 获取客户端请求中JSON格式的请求体
    data = request.json
    # 查看获取到的请求数据的类型
    print(type(data))
    # 获取请求体中对应字段的值
    name = data.get("name")
    age = data.get("age")
    return f"Name is {name}, age is {age}"


@app.route("/login", methods=["POST"])
def login():
    # 获取客户端请求中表单格式的请求体
    user_info = request.form
    # 查看请求数据的格式
    print(type(user_info))
    # 提取表单格式请求体中需要的数据
    username = user_info.get("username")
    password = user_info.get("password")
    return f"Welcome {username}"


@app.route("/upload", methods=["POST"])
def upload_file():
    # 获取客户端请求中提交的文件
    file = request.files
    # 查看获取的文件类型
    print(type(file))
    # 获取请求体中对应字段的值
    f = file.get("file")
    # 保存文件  uploads 这个目录提前创建好 secure_filename() 保证文件名安全
    f.save("./uploads/" + secure_filename(f.filename))
    return f"File {f.filename} is saved."


@app.route("/uploads", methods=["GET", "POST"])
def upload_files():
    # 获取客户端请求url
    r_url = request.url
    # 获取客户端请求域名
    r_host = request.host
    # 获取客户端请求的头信息
    r_headers = request.headers
    # 获取客户端请求方法
    r_method = request.method
    print(r_url, r_host, r_headers, r_method)
    # 获取文件请求体
    r_file = request.files
    # 判断请求方法为POST 的时候再进行保存文件操作
    if r_method == "POST":
        # 判断请求头信息中必须要包含My_Header 字段，并且值为hogwarts 提测需求
        if r_headers.get("My-Header") == "hogwarts":
            # 保存文件
            f = r_file.get("file")
            f.save("./uploads/" + secure_filename(f.filename))
            return f"File {f.filename} is saved."
        return "My-Header is wrong."
    return "Method is wrong."


if __name__ == '__main__':
    app.run()
