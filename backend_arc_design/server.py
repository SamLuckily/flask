# -*- coding : utf-8
# @Time: 2025-05-07
from flask import Flask
from flask_restx import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker, Session


class Base(DeclarativeBase):
    pass


# 声明基类
# Base = declarative_base()
# 创建引擎，连接到数据库
username = "root"
pwd = "123456"
ip = "127.0.0.1"
port = "3306"
database = "courses"
engine = create_engine(f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}')
# 创建session对象，绑定到数据库引擎上
DBSession = sessionmaker(bind=engine)
db_session: Session = DBSession()

app = Flask(__name__)

if __name__ == '__main__':
    from backend_arc_design.controller.course_controller import course_router

    app.register_blueprint(course_router)
    app.run(port=5055, debug=True)
