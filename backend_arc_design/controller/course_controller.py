# -*- coding : utf-8
# @Time: 2025-05-10
# 获取service的实例
import logging
from flask import Blueprint, request
from pydantic import ValidationError
from backend_arc_design.dto.course_dto import CourseDto
from backend_arc_design.service.course_service import CourseService

# 获取service的实例
course_service: CourseService = CourseService()

# 定义蓝图
course_router = Blueprint("course", __name__, url_prefix="/course")


@course_router.post("")
def create_course():
    # 获取json格式请求体
    course_info = request.json
    # 校验请求数据
    try:
        # 校验参数是否正常
        CourseDto.model_validate(course_info)
        # 新增课程
        course_id = course_service.create(course_info)
        return {
            "errcode": 0,
            "errmsg": "创建课程成功",
            "data": {
                "id": course_id
            }
        }
    except ValidationError as ve:
        logging.error(ve.errors())
        return {
            "errcode": 10002,
            "errmsg": "数据不符合规则"
        }
    except Exception as e:
        logging.error(e)
        return {
            "errcode": 10009,
            "errmsg": "服务出现错误"
        }


@course_router.get("/<int:course_id>")
def get_course(course_id):
    try:
        course = course_service.get(course_id)
        if course is None:
            return {
                "errcode": 10001,
                "errmsg": "课程不存在"
            }
        # 通过pydantic把查询结果对象转为字典格式
        datas = CourseDto.model_validate(course).model_dump()
        return {
            "errcode": 0,
            "errmsg": "获取课程信息成功",
            "datas": datas
        }
    except Exception as e:
        logging.error(e)
        return {
            "errcode": 10009,
            "errmsg": "服务出现错误"
        }


@course_router.get("/list")
def list_course():
    try:
        course_list = course_service.list()
        # 使用列表推导式获取全部数据列表，列表当中包含的字典格式数据
        datas = [CourseDto.model_validate(c).model_dump() for c in course_list]
        return {
            "errcode": 0,
            "errmsg": "获取全部课程信息列表成功",
            "datas": datas
        }
    except Exception as e:
        logging.error(e)
        return {
            "errcode": 10009,
            "errmsg": "服务出现错误"
        }


@course_router.put("")
def update_course():
    # 获取json格式请求体
    course_info = request.json
    # 校验请求数据
    try:
        # 校验参数是否正常
        CourseDto.model_validate(course_info)
        # 更新课程
        course_id = course_service.update(course_info)
        return {
            "errcode": 0,
            "errmsg": "课程更新成功",
            "data": {
                "id": course_id
            }
        }
    except ValidationError as ve:
        logging.error(ve.errors())
        return {
            "errcode": 10002,
            "errmsg": "数据不符合规则"
        }
    except Exception as e:
        logging.error(e)
        return {
            "errcode": 10009,
            "errmsg": "服务出现错误"
        }


@course_router.delete("/<int:course_id>")
def delete_course(course_id):
    try:
        course = course_service.get(course_id)
        if course is None:
            return {
                "errcode": 10001,
                "errmsg": "课程不存在"
            }
        course_service.delete(course_id)
        return {
            "errcode": 0,
            "errmsg": "课程删除成功",
            "data": {
                "id": course_id
            }
        }
    except Exception as e:
        logging.error(e)
        return {
            "errcode": 10009,
            "errmsg": "服务出现错误"
        }
