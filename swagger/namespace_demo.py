# -*- coding : utf-8
# @Time: 2025-05-11
from flask import Flask
from flask_restx import Resource, Api, Namespace

app = Flask(__name__)
api = Api(app)
# 定义命名空间
demo = Namespace("demo", description='demo学习')
case = Namespace("case", description='case练习')


# @api.route('/case')
# 定义子路由,如果没有的话，传空字符串即可
@case.route("")
class Case(Resource):
    # 定义restful 风格的方法
    def get(self):
        return {'code': 0, 'msg': 'get success'}

    def post(self):
        return {'code': 0, 'msg': 'post success'}

    def put(self):
        return {'code': 0, 'msg': 'put success'}

    def delete(self):
        return {'code': 0, 'msg': 'delete success'}


# @api.route('/demo')
@demo.route("")
class Demo(Resource):
    # 定义restful 风格的方法
    def get(self):
        return {'code': 0, 'msg': 'get success'}

    def post(self):
        return {'code': 0, 'msg': 'post success'}

    def put(self):
        return {'code': 0, 'msg': 'put success'}

    def delete(self):
        return {'code': 0, 'msg': 'delete success'}


# 添加命名空间，并指定空间路径
api.add_namespace(demo, '/demo')
api.add_namespace(case, '/case')
if __name__ == '__main__':
    app.run(debug=True)
