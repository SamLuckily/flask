# -*- coding : utf-8
# @Time: 2025-05-07
from typing import Optional

from flask import Flask, Blueprint, request
from pydantic import BaseModel, ConfigDict, constr, ValidationError
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 声明基类
Base = declarative_base()

# 创建引擎，连接到数据库
username = "root"
pwd = "123456"
ip = "127.0.0.1"
port = "3306"
database = "course"
engine = create_engine(f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}')
# 创建session对象，绑定到数据库引擎上
DBSession = sessionmaker(bind=engine)
# 获取会话实例
db_session: Session = DBSession()

# 定义app
app = Flask(__name__)


# 定义课程表结构
class Course(Base):
    __tablename__ = "t_course"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    detail = Column(String(255), default="")

    def __repr__(self):
        return f"<Course id: {self.id}, name: {self.name}>"


# 定义pydantic 对象，用于数据验证与解析
class CourseModel(BaseModel):
    # 可以通过其他类的实例自动生成并初始化出一个 pydantic 实例
    model_config = ConfigDict(from_attributes=True)
    # 制定校验规则
    id: int
    name: constr(max_length=30, min_length=1)
    detail: Optional[constr(max_length=255)] = ""


# 实现课程管理增删改查接口
# 使用蓝图管理路由
course_manager = Blueprint("course", __name__, url_prefix="/course")


# 新增课程接口
# 定义路由
@course_manager.post("")
def create_course():
    # 接收json格式的请求体
    course_json = request.get_json()
    print(f"请求体为{course_json}")
    # 验证请求体的数据是否符合需求
    try:
        # 使用pydantic 把请求参数转为 pydantic 对象
        CourseModel.model_validate(course_json)
    except ValidationError as e:
        # 如果转换出错， 代表传入的参数不符合需求
        print(e)
        return {
            "errcode": 10002,
            # repr 返回对象的字符串格式
            # e.errors() 返回错误列表
            "errmsg": repr(e.errors())
        }
    # 通过传入信息构造课程对象
    course = Course(**course_json)
    # 添加到数据库
    db_session.add(course)
    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()
    return {
        "errcode": 0,
        "errmsg": "创建课程成功"
    }


# 获取课程
@course_manager.get(f"/<int:course_id>")
def get_course(course_id: int):
    print(f"要获取的课程id 为 {course_id}")
    # 通过课程id 在数据库中查询
    course_data = db_session.query(Course).filter_by(id=course_id).first()
    # 如果查询结果为空
    if course_data is None:
        return {
            "errcode": 10001,
            "errmsg": "课程不存在"
        }
    # 通过pydantic 把查询结果对象转为字典格式
    datas = CourseModel.model_validate(course_data).model_dump()
    print(f"数据转换结果为 {datas}, 数据类型为 {type(datas)}")
    # 关闭连接
    db_session.close()
    return {
        "errcode": 0,
        "errmsg": f"获取 ID 为 {course_id} 的课程信息成功",
        "datas": datas
    }


# 获取全部课程信息列表
@course_manager.get("/list")
def get_courses():
    # 查询数据表，获取全部课程信息
    course_datas = db_session.query(Course).all()
    print(f"获取到的全部课程列表为 {course_datas}")
    # 获取所有查询结果字典格式的列表
    datas = [CourseModel.model_validate(course).model_dump() for course in course_datas]
    print(f"获取到的列表为 {datas}")
    db_session.close()
    return {
        "errcode": 0,
        "errmsg": "获取全部课程列表成功",
        "datas": datas
    }


# 修改课程
@course_manager.put("")
def update_course():
    # 获取json格式请求体
    course_json = request.get_json()
    print(f"请求体为 {course_json}")
    # 验证请求体是否符合需求
    try:
        CourseModel.model_validate(course_json)
    except ValidationError as e:
        print(e)
        return {
            "errcode": 10002,
            "errmsg": repr(e.errors())
        }
    # 构造课程对象
    course = Course(**course_json)
    # 根据课程id 查询，如果找不到结果则返回提示信息
    if db_session.query(Course).filter_by(id=course.id).first() is None:
        return {
            "errcode": 10001,
            "errmsg": "课程不存在"
        }
    # 使用pydantic 把请求数据转换为字典
    data = CourseModel.model_validate(course_json).model_dump()
    # 完成数据库更新
    db_session.query(Course).filter_by(id=course.id).update(data)
    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()
    return {
        "errcode": 0,
        "errmsg": "课程修改成功"
    }


# 删除课程
@course_manager.delete(f"<int:course_id>")
def delete_course(course_id: int):
    print(f"要删除的课程id为 {course_id}")
    # 根据id 查询
    course_data = db_session.query(Course).filter_by(id=course_id).first()
    # 判断查询结果，如果为空，则返回课程不存在
    if course_data is None:
        return {
            "errcode": 10001,
            "errmsg": "课程不存在"
        }
    # 删除查找到的课程
    db_session.delete(course_data)
    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()
    return {
        "errcode": 0,
        "errmsg": "课程删除成功"
    }


if __name__ == '__main__':
    # 创建表
    # Base.metadata.create_all(engine)
    # 启动app
    app.register_blueprint(course_manager)
    app.run(debug=True, port=5055)
