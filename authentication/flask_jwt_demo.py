# -*- coding : utf-8
# @Time: 2025-05-10
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


# 声明一个用户类
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


# 使用硬编码的凡事保存用户数据，实际数据来源一般是数据库
users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

# 获取所有用户的用户名
username_table = {u.username: u for u in users}
# 获取所有用户的id
userid_table = {u.id: u for u in users}


# 编写鉴权函数
def authenticate(username, password):
    # 通过用户名查询用户是否存在
    user = username_table.get(username, None)
    # 验证用户密码是否和数据库中的一致
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


# 编写返回哟个户标识的函数
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.debug = True
# 配置jwt密钥
app.config['SECRET_KEY'] = 'super-secret'
# 与flask应用做绑定
jwt = JWT(app, authenticate, identity)


# 需要鉴权的接口加上装饰器@jwt_required()
@app.route('/protected')
@jwt_required()
def protected():
    print(current_identity)
    return '%s' % current_identity


if __name__ == '__main__':
    app.run()
