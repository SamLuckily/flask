# -*- coding : utf-8
# @Time: 2025-05-11
from flask import Flask
from flask_restx import Resource, Api, Namespace, fields

app = Flask(__name__)
# 自定义版本号
api = Api(app, version="2.0")
# 定义命名空间
demo = Namespace("demo", description='demo学习')


@demo.route("")
class Demo(Resource):
    # 传递参数
    @demo.doc(params={'id': 'ID'})
    def get(self):
        return {'code': 0, 'msg': 'get success'}

    # 定义body数据
    post_model = api.model('PostModel', {
        # 定义post请求对应的数据
        # description描述信息
        # required约束是否为必填项
        'name': fields.String(description='The name', required=True),
        # enum 枚举型，只允许在给定的值里选择，限制不是很强，选C也可以请求成功
        'type': fields.String(description='The object type', enum=['A', 'B']),
        # int类型，min属性指定最小值
        'age': fields.Integer(min=0),
    })

    @demo.doc(body=post_model)
    def post(self):
        return {'code': 0, 'msg': 'post success'}


# 添加命名空间，并指定空间路径
api.add_namespace(demo, '/demo')
if __name__ == '__main__':
    app.run(debug=True)
