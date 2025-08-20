# -*- coding : utf-8
# @Time: 2025-05-11
from flask import Flask, request
from flask_restx import Resource, Api, Namespace, fields

from log_utils import logger

app = Flask(__name__)
# 自定义版本号
api = Api(app, version="2.0")
case = Namespace("case", description='case练习')


@case.route("")
class Case(Resource):
    # 定义parser解析器对象
    get_parser = api.parser()
    # 添加测试参数
    # location的值对应request对象的一些属性
    get_parser.add_argument('id', type=int, location='args', required=True)
    get_parser.add_argument('name', type=str, location='args')

    @api.expect(get_parser)
    def get(self):
        logger.info(f'request.args ==>{request.args}')
        return {'code': 0, 'msg': 'get success'}

    post_parser = api.parser()
    # post_parser.add_argument('username', type=str, help='username', location='form')
    # post_parser.add_argument('password', type=str, help='password', location='form')
    # post_parser.add_argument('id', type=int, location='json', required=True)
    # post_parser.add_argument('name', type=str, location='json', required=True)
    # post_parser.add_argument('file', type=FileStorage, location='files', required=True)
    post_parser.add_argument('choice', choices=("1", "2"), location='args')

    @api.expect(post_parser)
    def post(self):
        # logger.info(f"request.form ==>{request.form}")
        # logger.info(f"request.files ==>{request.files}")
        # choice格式
        logger.info(f"request.json ==>{request.args}")
        # logger.info(f"request.json ==>{request.json}")
        return {'code': 0, 'msg': 'post success'}


api.add_namespace(case, '/case')

if __name__ == '__main__':
    app.run(debug=True)
