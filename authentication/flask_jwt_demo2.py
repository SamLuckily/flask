# -*- coding : utf-8
# @Time: 2025-05-10
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)


# 声明一个用户类
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"User(id='{self.id}', username='{self.username}')"


# 模拟数据库
users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

# 获取所有用户的用户名
username_table = {u.username: u for u in users}
# 获取所有用户的id
userid_table = {u.id: u for u in users}

app = Flask(__name__)
app.debug = True
app.config['JWT_SECRET_KEY'] = 'super-secret'  # 配置 JWT 密钥
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)  # Token 有效时间为5分钟， 默认15分钟

jwt = JWTManager(app)  # 初始化扩展


# 登录接口：生成 token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = username_table.get(username, None)

    if user and user.password == password:
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token)
    else:
        return jsonify(msg='用户名或密码错误'), 401


# 受保护接口：必须携带有效 token
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = int(get_jwt_identity())
    user = userid_table.get(current_user_id)
    return jsonify(id=user.id, username=user.username)


if __name__ == '__main__':
    app.run()
