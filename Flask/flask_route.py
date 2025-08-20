# -*- coding : utf-8
# @Time: 2025-04-15


from flask import Flask

# 创建Flask应用程序实例
app = Flask(__name__)


# 定义基本路由
@app.route("/")
def index():
    return "Home Page"


@app.route("/about")
def about():
    return "About Page"


# 路由自动重定向
@app.route("/yl/")
def hello_yl():
    return "Hello YL"


# 定义动态路由
@app.route("/user/<username>")
def user_info(username):
    return f"User {username} is select info."


# 限定类型的动态路由
@app.route("/user/<int:userId>")
def user_id(userId):
    # 展示给定用户的ID, ID为整型
    return f"User ID is {userId}"


# 类型限定为path (可以包含 /)
@app.route("/path/<path:sub_path>")
def show_subpath(sub_path):
    # 展示path 后面的子路由
    return f"Subpath is {sub_path}"


# 运行应用程序
if __name__ == '__main__':
    app.run()
